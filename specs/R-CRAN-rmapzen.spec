%global packname  rmapzen
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Client for 'Mapzen' and Related Map APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.6.2
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-geojsonio 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf >= 0.6.2
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-geojsonio 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-maptools 
Requires:         R-utils 

%description
Provides an interface to 'Mapzen'-based APIs (including geocode.earth,
Nextzen, and NYC GeoSearch) for geographic search and geocoding, isochrone
calculation, and vector data to draw map tiles. See
<https://mapzen.com/documentation/> for more information. The original
Mapzen has gone out of business, but 'rmapzen' can be set up to work with
any provider who implements the Mapzen API.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
