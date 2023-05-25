%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgeos
%global packver   0.6-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to Geometry Engine - Open Source ('GEOS')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    geos-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Interface to Geometry Engine - Open Source ('GEOS') using the C 'API' for
topology operations on geometries. Please note that 'rgeos' will be
retired during October 2023, plan transition to 'sf' or 'terra' functions
using 'GEOS' at your earliest convenience (see
<https://r-spatial.org/r/2023/05/15/evolution4.html> and earlier blogs for
guidance). The 'GEOS' library is external to the package, and, when
installing the package from source, must be correctly installed first.
Windows and Mac Intel OS X binaries are provided on 'CRAN'. ('rgeos' >=
0.5-1): Up to and including 'GEOS' 3.7.1, topological operations succeeded
with some invalid geometries for which the same operations fail from and
including 'GEOS' 3.7.2. The 'checkValidity=' argument defaults and
structure have been changed, from default FALSE to integer default '0L'
for 'GEOS' < 3.7.2 (no check), '1L' 'GEOS' >= 3.7.2 (check and warn). A
value of '2L' is also provided that may be used, assigned globally using
'set_RGEOS_CheckValidity(2L)', or locally using the 'checkValidity=2L'
argument, to attempt zero-width buffer repair if invalid geometries are
found. The previous default (FALSE, now '0L') is fastest and used for
'GEOS' < 3.7.2, but will not warn users of possible problems before the
failure of topological operations that previously succeeded. From 'GEOS'
3.8.0, repair of geometries may also be attempted using 'gMakeValid()',
which may, however, return a collection of geometries of different types.

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
