%global packname  rcrimeanalysis
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          An Implementation of Crime Analysis Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-pals 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leafsync 
Requires:         R-CRAN-lubridate 
Requires:         R-KernSmooth 
Requires:         R-CRAN-pals 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
An implementation of functions for the analysis of crime incident or
records management system data. The package implements analysis algorithms
scaled for city or regional crime analysis units. The package provides
functions for kernel density estimation for crime heat maps, geocoding
using the 'Google Maps' API, identification of repeat crime incidents,
spatio-temporal map comparison across time intervals, time series analysis
(forecasting and decomposition), detection of optimal parameters for the
identification of near repeat incidents, and near repeat analysis with
crime network linkage.

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
%{rlibdir}/%{packname}/INDEX
