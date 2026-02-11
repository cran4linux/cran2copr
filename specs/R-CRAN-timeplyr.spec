%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timeplyr
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Tidy Tools for Date and Date-Time Manipulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-collapse >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.9.0
BuildRequires:    R-CRAN-pillar >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-cheapr >= 1.3.2
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-fastplyr >= 0.9.9
BuildRequires:    R-CRAN-vctrs >= 0.6.0
BuildRequires:    R-CRAN-cppdoubles >= 0.2.0
BuildRequires:    R-CRAN-timechange >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cpp11 
BuildRequires:    R-CRAN-tzdb 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-collapse >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.9.0
Requires:         R-CRAN-pillar >= 1.7.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-cheapr >= 1.3.2
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-fastplyr >= 0.9.9
Requires:         R-CRAN-vctrs >= 0.6.0
Requires:         R-CRAN-cppdoubles >= 0.2.0
Requires:         R-CRAN-timechange >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-scales 

%description
A set of fast tidy functions for wrangling, completing and summarising
date and date-time data. It combines 'tidyverse' syntax with the
efficiency of 'data.table' and speed of 'collapse'.

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
