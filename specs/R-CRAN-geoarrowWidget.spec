%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoarrowWidget
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Attach '(Geo)Arrow' and/or '(Geo)Parquet' Data to a Widget

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-listviewer 
BuildRequires:    R-CRAN-nanoarrow 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-listviewer 
Requires:         R-CRAN-nanoarrow 

%description
Provides functions and necessary 'JavaScript' bindings to quickly transfer
spatial data from R memory or remote URLs to the browser for use in
interactive 'HTML' widgets created with the 'htmlwidgets' R package.
Leverages 'GeoArrow' (<https://geoarrow.org/>) data representation for
data stored in local R memory which is generally faster than traditional
'GeoJSON' by minimising the amount of copy, serialization and
deserialization steps necessary for the data transfer. Furthermore,
provides functionality and 'JavaScript' bindings to consume 'GeoParquet'
(<https://geoparquet.org/>) files from remote URLs in the browser.

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
