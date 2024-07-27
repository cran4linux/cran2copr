%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weatherOz
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          An API Client for Australian Weather and Climate Data Resources

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.1.5
BuildRequires:    R-CRAN-apsimx 
BuildRequires:    R-CRAN-clock 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-data.table >= 1.1.5
Requires:         R-CRAN-apsimx 
Requires:         R-CRAN-clock 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-foreign 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magick 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Provides automated downloading, parsing and formatting of weather data for
Australia through API endpoints provided by the Department of Primary
Industries and Regional Development ('DPIRD') of Western Australia and by
the Science and Technology Division of the Queensland Government's
Department of Environment and Science ('DES'). As well as the Bureau of
Meteorology ('BOM') of the Australian government precis and coastal
forecasts, agriculture bulletin data, and downloading and importing radar
and satellite imagery files. 'DPIRD' weather data are accessed through
public 'APIs' provided by 'DPIRD',
<https://www.agric.wa.gov.au/weather-api-20>, providing access to weather
station data from the 'DPIRD' weather station network.  Australia-wide
weather data are based on data from the Australian Bureau of Meteorology
('BOM') data and accessed through 'SILO' (Scientific Information for Land
Owners) Jeffrey et al. (2001) <doi:10.1016/S1364-8152(01)00008-1>.
'DPIRD' data are made available under a Creative Commons Attribution 3.0
Licence (CC BY 3.0 AU) license
<https://creativecommons.org/licenses/by/3.0/au/deed.en>. SILO data are
released under a Creative Commons Attribution 4.0 International licence
(CC BY 4.0) <https://creativecommons.org/licenses/by/4.0/>. 'BOM' data are
(c) Australian Government Bureau of Meteorology and released under a
Creative Commons (CC) Attribution 3.0 licence or Public Access Licence
('PAL') as appropriate, see <http://www.bom.gov.au/other/copyright.shtml>
for further details.

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
