%global packname  rpostgisLT
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Managing Animal Movement Data with 'PostGIS' and R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpostgis >= 1.0.3
BuildRequires:    R-CRAN-adehabitatLT >= 0.3.12
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-rpostgis >= 1.0.3
Requires:         R-CRAN-adehabitatLT >= 0.3.12
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 

%description
Integrates R and the 'PostgreSQL/PostGIS' database system to build and
manage animal trajectory (movement) data sets. The package relies on
'ltraj' objects from the R package 'adehabitatLT', building the analogous
'pgtraj' data structure in 'PostGIS'. Functions allow users to seamlessly
transfer between 'ltraj' and 'pgtraj', as well as build new 'pgtraj'
directly from location data stored in the database.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples.R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shinyapp
%doc %{rlibdir}/%{packname}/sql
%{rlibdir}/%{packname}/INDEX
