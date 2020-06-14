%global packname  marmap
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          Import, Plot and Analyze Bathymetric and Topographic Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-adehabitatMA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-adehabitatMA 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Import xyz data from the NOAA (National Oceanic and Atmospheric
Administration, <http://www.noaa.gov>), GEBCO (General Bathymetric Chart
of the Oceans, <http://www.gebco.net>) and other sources, plot xyz data to
prepare publication-ready figures, analyze xyz data to extract transects,
get depth / altitude based on geographical coordinates, or calculate
z-constrained least-cost paths.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
