%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greed
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering and Model Selection with the Integrated Classification Likelihood

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-listenv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-cba 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-future 
Requires:         R-CRAN-listenv 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-RSpectra 
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-cba 
Requires:         R-CRAN-cli 

%description
An ensemble of algorithms that enable the clustering of networks and data
matrices (such as counts, categorical or continuous) with different type
of generative models. Model selection and clustering is performed in
combination by optimizing the Integrated Classification Likelihood (which
is equivalent to minimizing the description length). Several models are
available such as: Stochastic Block Model, degree corrected Stochastic
Block Model, Mixtures of Multinomial, Latent Block Model. The optimization
is performed thanks to a combination of greedy local search and a genetic
algorithm (see <arXiv:2002:11577> for more details).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
