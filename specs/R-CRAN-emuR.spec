%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  emuR
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Main Package of the EMU Speech Database Management System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 3.4.0
BuildRequires:    R-CRAN-cli >= 2.5.0
BuildRequires:    R-CRAN-RSQLite >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-httpuv >= 1.3.2
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-mime >= 0.6
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-wrassp >= 0.1.4
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-V8 >= 3.4.0
Requires:         R-CRAN-cli >= 2.5.0
Requires:         R-CRAN-RSQLite >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-httpuv >= 1.3.2
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-mime >= 0.6
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-wrassp >= 0.1.4
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-shiny 

%description
Provide the EMU Speech Database Management System (EMU-SDMS) with database
management, data extraction, data preparation and data visualization
facilities. See <https://ips-lmu.github.io/The-EMU-SDMS-Manual/> for more
details.

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
