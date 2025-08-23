%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vapour
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access to the 'Geospatial Data Abstraction Library' ('GDAL')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel
BuildRequires:    proj-devel
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-nanoarrow 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wk 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-nanoarrow 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-wk 

%description
Provides low-level access to 'GDAL' functionality. 'GDAL' is the
'Geospatial Data Abstraction Library' a translator for raster and vector
geospatial data formats that presents a single raster abstract data model
and single vector abstract data model to the calling application for all
supported formats <https://gdal.org/>. This package is focussed on
providing exactly and only what GDAL does, to enable developing further
tools.

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
