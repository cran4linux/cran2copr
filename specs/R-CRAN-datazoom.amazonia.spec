%global __brp_check_rpaths %{nil}
%global packname  datazoom.amazonia
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simplify Access to Data from the Amazon Region

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-sidrar 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-geobr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-googledrive 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-sidrar 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-geobr 
Requires:         R-CRAN-sf 
Requires:         R-utils 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-googledrive 

%description
Functions to download and treat data regarding the Brazilian Amazon region
from a variety of official sources.

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
