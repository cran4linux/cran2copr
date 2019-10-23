%global packname  GeoMongo
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Geospatial Queries Using 'PyMongo'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-geojsonR 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-geojsonR 
Requires:         R-CRAN-data.table 

%description
Utilizes methods of the 'PyMongo' 'Python' library to initialize, insert
and query 'GeoJson' data (see <https://api.mongodb.com/python/current/#>
for more information on 'PyMongo'). Furthermore, it allows the user to
validate 'GeoJson' objects and to use the console for 'MongoDB' (bulk)
commands. The 'reticulate' package provides the 'R' interface to 'Python'
modules, classes and functions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
