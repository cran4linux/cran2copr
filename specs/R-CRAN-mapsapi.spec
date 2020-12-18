%global packname  mapsapi
%global packver   0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          'sf'-Compatible Interface to 'Google Maps' APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-RgoogleMaps 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-RgoogleMaps 

%description
Interface to the 'Google Maps' APIs: (1) routing directions based on the
'Directions' API, returned as 'sf' objects, either as single feature per
alternative route, or a single feature per segment per alternative route;
(2) travel distance or time matrices based on the 'Distance Matrix' API;
(3) geocoded locations based on the 'Geocode' API, returned as 'sf'
objects, either points or bounds; (4) map images using the 'Maps Static'
API, returned as 'stars' objects.

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
