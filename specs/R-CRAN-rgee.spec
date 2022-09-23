%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgee
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          R Bindings for Calling the 'Earth Engine' API

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-reticulate >= 1.24
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-leafem 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-reticulate >= 1.24
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-leafem 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-cli 

%description
Earth Engine <https://earthengine.google.com/> client library for R. All
of the 'Earth Engine' API classes, modules, and functions are made
available. Additional functions implemented include importing (exporting)
of Earth Engine spatial objects, extraction of time series, interactive
map display, assets management interface, and metadata display. See
<https://r-spatial.github.io/rgee/> for further details.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python3@g' {} \;
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
