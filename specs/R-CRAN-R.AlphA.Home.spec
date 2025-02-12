%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R.AlphA.Home
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Feel at Home using R, Thanks to Shortcuts Functions Making it Simple

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-magrittr 

%description
A collection of personal functions designed to simplify and streamline
common R programming tasks. This package provides reusable tools and
shortcuts for frequently used calculations and workflows.

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
