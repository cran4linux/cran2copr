%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  leaflet.extras
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Functionality for 'leaflet' Package

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 

%description
The 'leaflet' JavaScript library provides many plugins some of which are
available in the core 'leaflet' package, but there are many more. It is
not possible to support them all in the core 'leaflet' package. This
package serves as an add-on to the 'leaflet' package by providing extra
functionality via 'leaflet' plugins.

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
