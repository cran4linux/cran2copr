%global packname  sf
%global packver   0.9-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          2%{?dist}
Summary:          Simple Features for R

License:          GPL-2 | MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 2.0.1
BuildRequires:    geos-devel >= 3.4.0
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-DBI >= 0.8
BuildRequires:    R-CRAN-units >= 0.6.0
BuildRequires:    R-CRAN-classInt >= 0.4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI >= 0.8
Requires:         R-CRAN-units >= 0.6.0
Requires:         R-CRAN-classInt >= 0.4.1
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Support for simple features, a standardized way to encode spatial vector
data. Binds to 'GDAL' for reading and writing data, to 'GEOS' for
geometrical operations, and to 'PROJ' for projection conversions and datum
transformations.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docker
%doc %{rlibdir}/%{packname}/gml
%doc %{rlibdir}/%{packname}/gpkg
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/nc
%doc %{rlibdir}/%{packname}/osm
%doc %{rlibdir}/%{packname}/shape
%doc %{rlibdir}/%{packname}/sqlite
%doc %{rlibdir}/%{packname}/tif
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
