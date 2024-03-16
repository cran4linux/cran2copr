%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  feasts
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Extraction and Statistics for Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.1
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.9.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-fabletools >= 0.3.1
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-slider 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-gtable 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 1.4.1
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.9.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-fabletools >= 0.3.1
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-lubridate 
Requires:         R-grid 
Requires:         R-CRAN-slider 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-gtable 

%description
Provides a collection of features, decomposition methods, statistical
summaries and graphics functions for the analysing tidy time series data.
The package name 'feasts' is an acronym comprising of its key features:
Feature Extraction And Statistics for Time Series.

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
