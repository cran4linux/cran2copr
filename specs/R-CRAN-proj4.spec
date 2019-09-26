%global packname  proj4
%global packver   1.0-8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8.1
Release:          1%{?dist}
Summary:          A simple interface to the PROJ.4 cartographic projectionslibrary

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    proj-devel >= 4.4.6
Requires:         proj
BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0

%description
A simple interface to lat/long projection and datum transformation of the
PROJ.4 cartographic projections library. It allows transformation of
geographic coordinates from one projection and/or datum to another.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}\
 --configure-vars='PKG_CPPFLAGS=-DACCEPT_USE_OF_DEPRECATED_PROJ_API_H'
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
