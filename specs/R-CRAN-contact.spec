%global packname  contact
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Creating Contact and Social Networks

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-parallel >= 3.6.0
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-foreach >= 1.4.8
BuildRequires:    R-CRAN-rgdal >= 1.4.4
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-rgeos >= 0.4.3
Requires:         R-CRAN-ape >= 5.3
Requires:         R-parallel >= 3.6.0
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-foreach >= 1.4.8
Requires:         R-CRAN-rgdal >= 1.4.4
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-rgeos >= 0.4.3

%description
Process spatially- and temporally-discrete data into contact and social
networks, and facilitate network analysis by randomizing individuals'
movement paths and/or related categorical variables. To use this package,
users need only have a dataset containing spatial data (i.e.,
latitude/longitude, or planar x & y coordinates), individual IDs relating
spatial data to specific individuals, and date/time information relating
spatial locations to temporal locations. The functionality of this package
ranges from data "cleaning" via multiple filtration functions, to spatial
and temporal data interpolation, and network creation and analysis.
Functions within this package are not limited to describing interpersonal
contacts. Package functions can also identify and quantify "contacts"
between individuals and fixed areas (e.g., home ranges, water bodies,
buildings, etc.). As such, this package is an incredibly useful resource
for facilitating epidemiological, ecological, ethological and sociological
research.

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
