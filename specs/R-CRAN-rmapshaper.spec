%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmapshaper
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for 'mapshaper' for 'Geospatial' Operations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 6.0.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-geojsonsf >= 2.0.5
BuildRequires:    R-CRAN-sp >= 1.4.0
BuildRequires:    R-CRAN-jsonify >= 1.2.3
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-V8 >= 6.0.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-geojsonsf >= 2.0.5
Requires:         R-CRAN-sp >= 1.4.0
Requires:         R-CRAN-jsonify >= 1.2.3
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-methods 

%description
Edit and simplify 'geojson', 'Spatial', and 'sf' objects.  This is wrapper
around the 'mapshaper' 'JavaScript' library by Matthew Bloch
<https://github.com/mbloch/mapshaper/> to perform topologically-aware
polygon simplification, as well as other operations such as clipping,
erasing, dissolving, and converting 'multi-part' to 'single-part'
geometries.

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
