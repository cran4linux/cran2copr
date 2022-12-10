%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oncomsm
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multi-State Models for Early Oncology

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-rstan >= 2.18
BuildRequires:    R-CRAN-StanHeaders >= 2.18
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppNumerical >= 0.4
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.18
Requires:         R-CRAN-RcppNumerical >= 0.4
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-rstantools

%description
Implements methods to fit a parametric Bayesian multi-state model to tumor
response data. The model can be used to sample from the predictive
distribution to impute missing data and calculate probability of success
for custom decision criteria in early clinical trials during an ongoing
trial. The inference is implemented using 'stan'.

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
