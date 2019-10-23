%global packname  dtwSat
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Time-Weighted Dynamic Time Warping for Satellite Image TimeSeries Analysis

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-reshape2 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-caret 
Requires:         R-mgcv 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-Rdpack 

%description
Provides an implementation of the Time-Weighted Dynamic Time Warping
(TWDTW) method for land cover mapping using satellite image time series.
TWDTW is based on the Dynamic Time Warping technique and has achieved high
accuracy for land cover classification using satellite data. The method is
based on comparing unclassified satellite image time series with a set of
known temporal patterns (e.g. phenological cycles associated with the
vegetation). Using 'dtwSat' the user can build temporal patterns for land
cover types, apply the TWDTW analysis for satellite datasets, visualize
the results of the time series analysis, produce land cover maps, create
temporal plots for land cover change, and compute accuracy assessment
metrics.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/lucc_MT
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
