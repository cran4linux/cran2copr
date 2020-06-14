%global packname  aspace
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          2%{?dist}
Summary:          A collection of functions for estimating centrographicstatistics and computational geometries for spatial pointpatterns

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-shapefiles 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-shapefiles 

%description
A collection of functions for computing centrographic statistics (e.g.,
standard distance, standard deviation ellipse, standard deviation box) for
observations taken at point locations. Separate plotting functions have
been developed for each measure. Users interested in writing results to
ESRI shapefiles can do so by using results from aspace functions as inputs
to the convert.to.shapefile and write.shapefile functions in the
shapefiles library. The aspace library was originally conceived to aid in
the analysis of spatial patterns of travel behaviour (see Buliung and
Remmel, 2008). Major changes in the current version include (1) removal of
dependencies on several external libraries (e.g., gpclib, maptools, sp),
(2) the separation of plotting and estimation capabilities, (3) reduction
in the number of functions, and (4) expansion of analytical capabilities
with additional functions for descriptive analysis and visualization
(e.g., standard deviation box, centre of minimum distance, central
feature).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
