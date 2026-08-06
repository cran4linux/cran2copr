%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dwg2geo
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Engineering 'DWG' Drawings to Auditable 'GeoJSON'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Converts engineering 'DWG' drawings ('AutoCAD' 2013+ format) to 'GeoJSON'
entirely in-process, with no 'CAD' software, 'LibreDWG', or 'GDAL'
required. Wraps the pure-Rust 'dwg2geo' conversion core
<https://github.com/milkway/dwg2geo>: every feature carries resolved 'CAD'
style metadata (layer, colour, line weight, text), skipped and failed
entities are reported with reasons, and the output is deterministic: the
same bytes always produce byte-identical 'GeoJSON'. Coordinates are kept
in the drawing's local system; the package never guesses a coordinate
reference system.

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
