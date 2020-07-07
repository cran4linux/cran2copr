%global packname  leafgl
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
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
