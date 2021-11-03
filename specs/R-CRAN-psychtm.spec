%global __brp_check_rpaths %{nil}
%global packname  psychtm
%global packver   2021.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2021.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Text Mining Methods for Psychological Research

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-RcppProgress >= 0.4.2
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-coda >= 0.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-coda >= 0.4
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-label.switching 
Requires:         R-methods 

%description
Provides text mining methods for social science research. The package
implements estimation, inference, summarization, and goodness-of-fit
methods for topic models including Latent Dirichlet Allocation (LDA),
supervised LDA, and supervised LDA with covariates using Bayesian Markov
Chain Monte Carlo. A description of the key models and estimation methods
is available in Wilcox, Jacobucci, Zhang, & Ammerman (2021).
<doi:10.31234/osf.io/62tc3>.

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
