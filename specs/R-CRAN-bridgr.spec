%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bridgr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bridging Data Frequencies for Timely Economic Forecasts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tsbox 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tsbox 
Requires:         R-CRAN-withr 

%description
Implements bridge and MIDAS-style mixed-frequency models for nowcasting
and forecasting macroeconomic variables by linking higher-frequency
indicator variables to a lower-frequency target series. The package
standardizes input data, infers regular frequencies, forecasts missing
indicator observations, and aggregates indicators to the target frequency
before fitting a regression with autoregressive target dynamics. Frequency
alignment can be customized through user-supplied conversion rules. For
more on bridge and MIDAS models, see Baffigi, A., Golinelli, R., & Parigi,
G. (2004) <doi:10.1016/S0169-2070(03)00067-0>, Ghysels, Sinko, & Valkanov
(2007) <doi:10.1080/07474930600972467>, Andreou, Ghysels, & Kourtellos
(2010) <doi:10.1016/j.jeconom.2010.01.004>, Schumacher (2016)
<doi:10.1016/j.ijforecast.2015.07.004>, and Burri (2026)
<doi:10.1111/obes.70073>.

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
