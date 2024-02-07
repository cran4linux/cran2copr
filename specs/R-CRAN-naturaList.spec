%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  naturaList
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Classify Occurrences by Confidence Levels in the Species ID

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-htmltools 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-stringi 

%description
Classify occurrence records based on confidence levels of species
identification. In addition, implement tools to filter occurrences inside
grid cells and to manually check for possibles errors with an interactive
shiny application.

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
