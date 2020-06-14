%global packname  pleiades
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Interface to the 'Pleiades' 'Archeological' Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-RSQLite >= 1.1.2
BuildRequires:    R-CRAN-dbplyr >= 1.0.0
BuildRequires:    R-CRAN-DBI >= 0.6.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-gistr >= 0.4.0
BuildRequires:    R-CRAN-crul >= 0.3.6
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-RSQLite >= 1.1.2
Requires:         R-CRAN-dbplyr >= 1.0.0
Requires:         R-CRAN-DBI >= 0.6.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-gistr >= 0.4.0
Requires:         R-CRAN-crul >= 0.3.6
Requires:         R-CRAN-rappdirs 

%description
Provides a set of functions for interacting with the 'Pleiades'
(<https://pleiades.stoa.org/>) 'API', including getting status data,
places data, and creating a 'GeoJSON' based map on 'GitHub' 'gists'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
