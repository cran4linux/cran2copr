%global packname  bomrang
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Australian Government Bureau of Meteorology ('BOM') Data Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.8
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-janitor >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 2.8
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-janitor >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides functions to interface with Australian Government Bureau of
Meteorology ('BOM') data, fetching data and returning a data frame of
precis forecasts, historical and current weather data from stations,
agriculture bulletin data, 'BOM' 0900 or 1500 weather bulletins and
downloading and importing radar and satellite imagery files.  Data (c)
Australian Government Bureau of Meteorology Creative Commons (CC)
Attribution 3.0 licence or Public Access Licence (PAL) as appropriate.
See <http://www.bom.gov.au/other/copyright.shtml> for further details.

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
