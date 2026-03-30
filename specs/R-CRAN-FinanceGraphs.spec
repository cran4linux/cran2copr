%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FinanceGraphs
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Graphs for Analysis of Financial Data and Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate >= 4000
BuildRequires:    R-grDevices >= 4.5.0
BuildRequires:    R-stats >= 4.5.0
BuildRequires:    R-utils >= 4.5.0
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-cpm >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-knitr >= 1.45
BuildRequires:    R-CRAN-hexbin >= 1.28.0
BuildRequires:    R-CRAN-purrr >= 1.2.0
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-dygraphs >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tibble >= 1.0.0
BuildRequires:    R-CRAN-broom >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-CRAN-ggiraph >= 0.9.0
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-CRAN-ggtext >= 0.1.0
Requires:         R-CRAN-timeDate >= 4000
Requires:         R-grDevices >= 4.5.0
Requires:         R-stats >= 4.5.0
Requires:         R-utils >= 4.5.0
Requires:         R-graphics >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-cpm >= 2.0
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-knitr >= 1.45
Requires:         R-CRAN-hexbin >= 1.28.0
Requires:         R-CRAN-purrr >= 1.2.0
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-dygraphs >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tibble >= 1.0.0
Requires:         R-CRAN-broom >= 1.0.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-CRAN-ggiraph >= 0.9.0
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-CRAN-ggtext >= 0.1.0

%description
Flexible wrappers around R graphics modules 'dygraphs'
<https://dygraphs.com/> and 'ggplot2' <https://ggplot2.tidyverse.org/> to
visualize data commonly found in Financial Studies, with an emphasis on
time series. Interactive time series plots include multiple options for
incorporating external data such as forecasts and events.  Other static
plots useful for time series data include an intuitive and generic scatter
plotter, a boxplot generator suitable for multiple time series, and event
study plotters for time series analysis around sets of dates.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
