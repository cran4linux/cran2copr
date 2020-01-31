%global packname  vapour
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Lightweight Access to the 'Geospatial Data Abstraction Library'('GDAL')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 2.0.0
BuildRequires:    proj-devel >= 4.8.0
Requires:         gdal
Requires:         proj
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
Provides low-level access to 'GDAL' functionality for R packages. The aim
is to minimize the level of interpretation put on the 'GDAL' facilities,
to enable direct use of it for a variety of purposes. 'GDAL' is the
'Geospatial Data Abstraction Library' a translator for raster and vector
geospatial data formats that presents a single raster abstract data model
and single vector abstract data model to the calling application for all
supported formats <http://gdal.org/>. Other available packages 'rgdal' and
'sf' also provide access to the 'GDAL' library, but neither can be used
for these lower level tasks, and both do many other tasks.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmarks
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docker
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/pbf
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/stars
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
