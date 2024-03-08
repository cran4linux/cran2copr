%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastTS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Time Series Modeling for Seasonal Series with Exogenous Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-yardstick 

%description
An implementation of sparsity-ranked lasso and related methods for time
series data. This methodology is especially useful for large time series
with exogenous features and/or complex seasonality. Originally described
in Peterson and Cavanaugh (2022) <doi:10.1007/s10182-021-00431-7> in the
context of variable selection with interactions and/or polynomials, ranked
sparsity is a philosophy with methods useful for variable selection in the
presence of prior informational asymmetry. This situation exists for time
series data with complex seasonality, as shown in Peterson and Cavanaugh
(2023+) <doi:10.48550/arXiv.2211.01492>, which also describes this package
in greater detail. The sparsity-ranked penalization methods for Time
Series implemented in 'fastTS' can fit large/complex/high-frequency time
series quickly, even with a high-dimensional exogenous feature set. The
method is considerably faster than its competitors, while often producing
more accurate predictions. Also included is a long hourly series of
arrivals into the University of Iowa Emergency Department with concurrent
local temperature.

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
