%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toro
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Performance Interactive Mapping

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 

%description
Interactive spatial visualisations are a cornerstone for exploring and
communicating complexity, and are commonly embedded into reports or
interactive dashboards. However, as the amount of data grows, so do the
demands on functionality, especially for technical and scientific data. To
bridge this gap and create a mapping package that is high performing, a
modern approach is needed that draws from best software engineering
practices. Toro provides bindings to 'MapLibre GL JS', an open-source
'JavaScript'/'TypeScript' library for rendering interactive maps in the
browser, built from the ground up for responsiveness and scale, by the
MapLibre Organization (2020) <https://github.com/MapLibre>. This
connection allows users to create interactive maps that can easily be
integrated into both 'Quarto' and the 'R Shiny' dashboard framework. Toro
thereby enables spatial visualisation and exploration of data that might
otherwise be too limited, too slow, or too hard to scale using more
traditional interactive mapping tools such as 'leaflet'.

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
