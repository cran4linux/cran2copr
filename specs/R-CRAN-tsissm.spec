%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsissm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Innovations State Space Unobserved Components Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-TMB >= 1.7.20
BuildRequires:    R-CRAN-tsmethods >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tsaux 
BuildRequires:    R-CRAN-tsdistributions 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-RTMB 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.20
Requires:         R-CRAN-tsmethods >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-methods 
Requires:         R-CRAN-tsaux 
Requires:         R-CRAN-tsdistributions 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-RTMB 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 

%description
Unobserved components time series model using the linear innovations state
space representation (single source of error) with choice of error
distributions and option for dynamic variance. Methods for estimation
using automatic differentiation, automatic model selection and ensembling,
prediction, filtering, simulation and backtesting. Based on the model
described in Hyndman et al (2012) <doi:10.1198/jasa.2011.tm09771>.

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
