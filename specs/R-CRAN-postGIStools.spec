%global packname  postGIStools
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Interacting with 'PostgreSQL' / 'PostGIS' Databases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.2
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-rgdal >= 0.8
BuildRequires:    R-CRAN-DBI >= 0.5
BuildRequires:    R-CRAN-RPostgreSQL >= 0.4
BuildRequires:    R-CRAN-rgeos >= 0.3
BuildRequires:    R-methods 
Requires:         R-CRAN-sp >= 1.2
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-rgdal >= 0.8
Requires:         R-CRAN-DBI >= 0.5
Requires:         R-CRAN-RPostgreSQL >= 0.4
Requires:         R-CRAN-rgeos >= 0.3
Requires:         R-methods 

%description
Functions to convert geometry and 'hstore' data types from 'PostgreSQL'
into standard R objects, as well as to simplify the import of R data
frames (including spatial data frames) into 'PostgreSQL'. Note: This
package is deprecated. For new projects, we recommend using the 'sf'
package to interface with geodatabases.

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
%{rlibdir}/%{packname}/INDEX
