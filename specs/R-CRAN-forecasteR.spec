%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forecasteR
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Forecast System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-echarts4r 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinydashboardPlus >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-DT 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-config 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-echarts4r 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycustomloader 

%description
A web application for displaying, analysing and forecasting univariate
time series. Includes basic methods such as mean, naïve, seasonal naïve
and drift, as well as more complex methods such as Holt-Winters Box,G and
Jenkins, G (1976) <doi:10.1111/jtsa.12194> and ARIMA Brockwell, P.J. and
R.A.Davis (1991) <doi:10.1007/978-1-4419-0320-4>.

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
