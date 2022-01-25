%global __brp_check_rpaths %{nil}
%global packname  googleway
%global packver   2.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.6
Release:          1%{?dist}%{?buildtag}
Summary:          Accesses Google Maps APIs to Retrieve Data and Plot Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.20
BuildRequires:    R-CRAN-googlePolylines >= 0.7.1
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-jsonlite >= 0.9.20
Requires:         R-CRAN-googlePolylines >= 0.7.1
Requires:         R-CRAN-curl 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jpeg 
Requires:         R-utils 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 

%description
Provides a mechanism to plot a 'Google Map' from 'R' and overlay it with
shapes and markers. Also provides access to 'Google Maps' APIs, including
places, directions, roads, distances, geocoding, elevation and timezone.

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
