%global packname  greed
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering and Model Selection with the Integrated Classification Likelihood

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-listenv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-cba 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-future 
Requires:         R-CRAN-listenv 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-cba 

%description
An ensemble of algorithms that enable the clustering of networks and data
matrix such as counts matrix with different type of generative models.
Model selection and clustering is performed in combination by optimizing
the Integrated Classification Likelihood (which is equivalent to
minimizing the description length). Several models are available such as:
Stochastic Block Model, degree corrected Stochastic Block Model, Mixtures
of Multinomial, Latent Block Model. The optimization is performed thanks
to a combination of greedy local search and a genetic algorithm (see
<arXiv:2002:11577> for more details).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
