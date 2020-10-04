%global packname  animaltracker
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Animal Tracker

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-raster >= 2.7.15
BuildRequires:    R-CRAN-tibble >= 2.1.0
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-V8 >= 2.0
BuildRequires:    R-CRAN-zoo >= 1.8.6
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-geosphere >= 1.5.7
BuildRequires:    R-CRAN-rgdal >= 1.3.6
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-shinythemes >= 1.1.2
BuildRequires:    R-CRAN-leaflet.extras >= 1.0.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.4
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-shinycssloaders >= 0.2
BuildRequires:    R-CRAN-elevatr >= 0.2.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-raster >= 2.7.15
Requires:         R-CRAN-tibble >= 2.1.0
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-V8 >= 2.0
Requires:         R-CRAN-zoo >= 1.8.6
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-geosphere >= 1.5.7
Requires:         R-CRAN-rgdal >= 1.3.6
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-shinythemes >= 1.1.2
Requires:         R-CRAN-leaflet.extras >= 1.0.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-shinyWidgets >= 0.4.4
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-shinycssloaders >= 0.2
Requires:         R-CRAN-elevatr >= 0.2.0

%description
Utilities for spatial-temporal analysis and visualization of animal (e.g.
cattle) tracking data. The core feature is a 'shiny' web application for
customized processing of GPS logs, including features for data
augmentation (e.g. elevation lookup), data selection, export, plotting,
and statistical summaries. A data validation application allows for
side-by-side comparison via time series plots and extreme value detection
described by J.P. van Brakel
<https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data/>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
