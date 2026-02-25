%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AeRobiology
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Computational Tool for Aerobiological Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-ggvis 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-ggvis 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-CRAN-zoo 
Requires:         R-grid 
Requires:         R-CRAN-data.table 

%description
Different tools for managing databases of airborne particles, elaborating
the main calculations and visualization of results. In a first step, data
are checked using tools for quality control and all missing gaps are
completed. Then, the main parameters of the pollen season are calculated
and represented graphically. Multiple graphical tools are available:
pollen calendars, phenological plots, time series, tendencies, interactive
plots, abundance plots...

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
