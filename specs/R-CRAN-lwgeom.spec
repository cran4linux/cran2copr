%global packname  lwgeom
%global packver   0.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Bindings to Selected 'liblwgeom' Functions for Simple Features

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    geos-devel >= 3.3.0
BuildRequires:    proj-devel >= 4.8.0
Requires:         geos
Requires:         proj
Requires:         proj-nad
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-sf >= 0.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf >= 0.6.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-units 

%description
Access to selected functions found in 'liblwgeom'
<https://github.com/postgis/postgis/tree/svn-trunk/liblwgeom>, the
light-weight geometry library used by 'PostGIS' <http://postgis.net/>.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
