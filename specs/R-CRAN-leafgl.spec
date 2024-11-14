%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  leafgl
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          High-Performance 'WebGl' Rendering for Package 'leaflet'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonify 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-sf 
Requires:         R-grDevices 

%description
Provides bindings to the 'Leaflet.glify' JavaScript library which extends
the 'leaflet' JavaScript library to render large data in the browser using
'WebGl'.

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
