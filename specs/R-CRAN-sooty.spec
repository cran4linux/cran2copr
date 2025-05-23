%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sooty
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Source Catalogues Online for Southern Ocean Ecosystem Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-tibble 

%description
Obtains lists of files of remote sensing collections for Southern Ocean
surface properties. Commonly used data sources of sea surface temperature,
sea ice concentration, and altimetry products such as sea surface height
and sea surface currents are cached in object storage on the Pawsey
Supercomputing Research Centre facility. Patterns of working to retrieve
data from these object storage catalogues are described. The catalogues
include complete collections of datasets Reynolds et al. (2008) "NOAA
Optimum Interpolation Sea Surface Temperature (OISST) Analysis, Version
2.1" <doi:10.7289/V5SQ8XB5>, Spreen et al. (2008) "Artist Advanced
Microwave Scanning Radiometer for Earth Observing System (AMSR-E) sea ice
concentration" <doi:10.1029/2005JC003384>. In future releases helpers will
be added to identify particular data collections and target specific dates
for earth observation data for reading, as well as helpers to retrieve
data set citation and provenance details.  This work was supported by
resources provided by the Pawsey Supercomputing Research Centre with
funding from the Australian Government and the Government of Western
Australia.  This software was developed by the Integrated Digital East
Antarctica program of the Australian Antarctic Division.

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
