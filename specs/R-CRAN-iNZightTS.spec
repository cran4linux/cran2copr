%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iNZightTS
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series for 'iNZight'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-fable 
BuildRequires:    R-CRAN-fabletools 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-urca 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-glue 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-fable 
Requires:         R-CRAN-fabletools 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-urca 

%description
Provides a collection of functions for working with time series data,
including functions for drawing, decomposing, and forecasting. Includes
capabilities to compare multiple series and fit both additive and
multiplicative models. Used by 'iNZight', a graphical user interface
providing easy exploration and visualisation of data for students of
statistics, available in both desktop and online versions. Holt (1957)
<doi:10.1016/j.ijforecast.2003.09.015>, Winters (1960)
<doi:10.1287/mnsc.6.3.324>, Cleveland, Cleveland, & Terpenning (1990)
"STL: A Seasonal-Trend Decomposition Procedure Based on Loess".

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
