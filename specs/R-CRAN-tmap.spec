%global packname  tmap
%global packver   3.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Thematic Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tmaptools >= 3.1
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-sf >= 0.9.7
BuildRequires:    R-CRAN-units >= 0.6.1
BuildRequires:    R-CRAN-stars >= 0.5.0
BuildRequires:    R-CRAN-classInt >= 0.4.3
BuildRequires:    R-CRAN-leafem >= 0.1
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-widgetframe 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-tmaptools >= 3.1
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-sf >= 0.9.7
Requires:         R-CRAN-units >= 0.6.1
Requires:         R-CRAN-stars >= 0.5.0
Requires:         R-CRAN-classInt >= 0.4.3
Requires:         R-CRAN-leafem >= 0.1
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-widgetframe 
Requires:         R-CRAN-leafsync 
Requires:         R-stats 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

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
