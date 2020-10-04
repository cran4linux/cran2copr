%global packname  TSstudio
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Time Series Analysis and Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.2
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-forecastHybrid >= 2.0.10
BuildRequires:    R-CRAN-zoo >= 1.8.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-data.table >= 1.11.2
BuildRequires:    R-CRAN-future >= 1.10.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-future.apply >= 1.0.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.8.2
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-forecast >= 8.2
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-forecastHybrid >= 2.0.10
Requires:         R-CRAN-zoo >= 1.8.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-future >= 1.10.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-future.apply >= 1.0.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.8.2
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-xts >= 0.12.0

%description
Provides a set of tools for descriptive and predictive analysis of time
series data. That includes functions for interactive visualization of time
series objects and as well utility functions for automation time series
forecasting.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
