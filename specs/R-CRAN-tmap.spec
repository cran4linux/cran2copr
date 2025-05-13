%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmap
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Thematic Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tmaptools >= 3.1
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-cols4all >= 0.8
BuildRequires:    R-CRAN-units >= 0.6.1
BuildRequires:    R-CRAN-classInt >= 0.4.3
BuildRequires:    R-CRAN-stars >= 0.4.2
BuildRequires:    R-CRAN-leafem >= 0.2.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-leafgl 
BuildRequires:    R-CRAN-leaflegend 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-CRAN-maptiles 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-s2 
BuildRequires:    R-CRAN-servr 
Requires:         R-CRAN-tmaptools >= 3.1
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-cols4all >= 0.8
Requires:         R-CRAN-units >= 0.6.1
Requires:         R-CRAN-classInt >= 0.4.3
Requires:         R-CRAN-stars >= 0.4.2
Requires:         R-CRAN-leafem >= 0.2.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-leafgl 
Requires:         R-CRAN-leaflegend 
Requires:         R-CRAN-leafsync 
Requires:         R-CRAN-maptiles 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-s2 
Requires:         R-CRAN-servr 

%description
Thematic maps are geographical maps in which spatial data distributions
are visualized. This package offers a flexible, layer-based, and easy to
use approach to create thematic maps, such as choropleths and bubble maps.

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
