%global packname  hyfo
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Hydrology and Climate Forecasting

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.39
BuildRequires:    R-stats >= 3.1.3
BuildRequires:    R-utils >= 3.1.3
BuildRequires:    R-CRAN-lmom >= 2.5
BuildRequires:    R-CRAN-maps >= 2.3.9
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-ncdf4 >= 1.14
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-maptools >= 0.8.36
BuildRequires:    R-CRAN-rgdal >= 0.8.16
BuildRequires:    R-CRAN-rgeos >= 0.3.8
BuildRequires:    R-CRAN-moments >= 0.14
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-MASS >= 7.3.39
Requires:         R-stats >= 3.1.3
Requires:         R-utils >= 3.1.3
Requires:         R-CRAN-lmom >= 2.5
Requires:         R-CRAN-maps >= 2.3.9
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-ncdf4 >= 1.14
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-maptools >= 0.8.36
Requires:         R-CRAN-rgdal >= 0.8.16
Requires:         R-CRAN-rgeos >= 0.3.8
Requires:         R-CRAN-moments >= 0.14
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
Focuses on data processing and visualization in hydrology and climate
forecasting. Main function includes data extraction, data downscaling,
data resampling, gap filler of precipitation, bias correction of
forecasting data, flexible time series plot, and spatial map generation.
It is a good pre- processing and post-processing tool for hydrological and
hydraulic modellers.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
