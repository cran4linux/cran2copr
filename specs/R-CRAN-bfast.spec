%global __brp_check_rpaths %{nil}
%global packname  bfast
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Breaks for Additive Season and Trend

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-strucchangeRcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-strucchangeRcpp 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-forecast 

%description
Decomposition of time series into trend, seasonal, and remainder
components with methods for detecting and characterizing abrupt changes
within the trend and seasonal components. 'BFAST' can be used to analyze
different types of satellite image time series and can be applied to other
disciplines dealing with seasonal or non-seasonal time series, such as
hydrology, climatology, and econometrics. The algorithm can be extended to
label detected changes with information on the parameters of the fitted
piecewise linear models. 'BFAST' monitoring functionality is described in
Verbesselt et al. (2010) <doi:10.1016/j.rse.2009.08.014>. 'BFAST monitor'
provides functionality to detect disturbance in near real-time based on
'BFAST'- type models, and is described in Verbesselt et al. (2012)
<doi:10.1016/j.rse.2012.02.022>. 'BFAST Lite' approach is a flexible
approach that handles missing data without interpolation, and will be
described in an upcoming paper. Furthermore, different models can now be
used to fit the time series data and detect structural changes (breaks).

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
