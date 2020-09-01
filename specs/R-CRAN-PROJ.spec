%global packname  PROJ
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generic Coordinate System Transformations Using 'PROJ'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-libproj >= 7.1.0.1
Requires:         R-CRAN-libproj >= 7.1.0.1

%description
A wrapper around the generic coordinate transformation software 'PROJ'
that transforms geospatial coordinates from one coordinate reference
system ('CRS') to another. This includes cartographic projections as well
as geodetic transformations. Version 7.1.0-1 or higher of the R package
'libproj' is required. The intention is for this package to be used by
user-packages such as 'reproj', and that the older 'PROJ.4' and version 5
pathways be provided by the 'proj4' package. Separating this disruptive
version change (from 4.0 and 5.0, to 6.0 and above) allows the use of
existing and stable code in 'proj4' alongside the new idioms and
requirements of modern 'PROJ'. For control of metadata files for the
'PROJ' library, see tools in the 'libproj' package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
