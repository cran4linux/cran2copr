%global packname  rgeos
%global packver   0.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          3%{?dist}
Summary:          Interface to Geometry Engine - Open Source ('GEOS')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    geos-devel >= 3.2.0
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
topology operations on geometries. The 'GEOS' library is external to the
package, and, when installing the package from source, must be correctly
installed first. Windows and Mac Intel OS X binaries are provided on
'CRAN'. ('rgeos' >= 0.5-1): Up to and including 'GEOS' 3.7.1, topological
operations succeeded with some invalid geometries for which the same
operations fail from and including 'GEOS' 3.7.2. The 'checkValidity='
argument defaults and structure have been changed, from default FALSE to
integer default '0L' for 'GEOS' < 3.7.2 (no check), '1L' 'GEOS' >= 3.7.2
(check and warn). A value of '2L' is also provided that may be used,
assigned globally using 'set_RGEOS_CheckValidity(2L)', or locally using
the 'checkValidity=2L' argument, to attempt zero-width buffer repair if
invalid geometries are found. The previous default (FALSE, now '0L') is
fastest and used for 'GEOS' < 3.7.2, but will not warn users of possible
problems before the failure of topological operations that previously
succeeded. From 'GEOS' 3.8.0, repair of geometries may also be attempted
using 'gMakeValid()', which may, however, return a collection of
geometries of different types.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/poly-ex-gpc
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/SVN_VERSION
%doc %{rlibdir}/%{packname}/test_cases
%doc %{rlibdir}/%{packname}/wkts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
