%global __brp_check_rpaths %{nil}
%global packname  rmapshaper
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Client for 'mapshaper' for 'Geospatial' Operations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 3.4.2
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-sp >= 1.4.0
BuildRequires:    R-CRAN-geojsonio >= 0.9.4
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-geojsonlint >= 0.4.0
BuildRequires:    R-methods 
Requires:         R-CRAN-V8 >= 3.4.2
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-sp >= 1.4.0
Requires:         R-CRAN-geojsonio >= 0.9.4
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-geojsonlint >= 0.4.0
Requires:         R-methods 

%description
Edit and simplify 'geojson', 'Spatial', and 'sf' objects.  This is wrapper
around the 'mapshaper' 'JavaScript' library by Matthew Bloch
<https://github.com/mbloch/mapshaper/> to perform topologically-aware
polygon simplification, as well as other operations such as clipping,
erasing, dissolving, and converting 'multi-part' to 'single-part'
geometries.  It relies on the 'geojsonio' package for working with
'geojson' objects, the 'sf' package for working with 'sf' objects, and the
'sp' and 'rgdal' packages for working with 'Spatial' objects.

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
