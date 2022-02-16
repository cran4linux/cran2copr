%global __brp_check_rpaths %{nil}
%global packname  legion
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting Using Multivariate Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-smooth >= 3.1.0
BuildRequires:    R-CRAN-greybox >= 1.0.4
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.100.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-smooth >= 3.1.0
Requires:         R-CRAN-greybox >= 1.0.4
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-nloptr 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Functions implementing multivariate state space models for purposes of
time series analysis and forecasting. The focus of the package is on
multivariate models, such as Vector Exponential Smoothing, Vector ETS
(Error-Trend-Seasonal model) etc. It currently includes Vector Exponential
Smoothing (VES, de Silva et al., 2010, <doi:10.1177/1471082X0901000401>),
Vector ETS and simulation function for VES.

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
