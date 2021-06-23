%global __brp_check_rpaths %{nil}
%global packname  RTL
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Tool Library - Trading, Risk, Analytic for Commodities

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibbletime 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tidyquant 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-fabletools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-tidyverse 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibbletime 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tidyquant 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-fabletools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-tidyverse 

%description
Collection of functions and metadata to complement core packages in
Finance and Commodities, including futures expiry tables and
<https://www.morningstar.com/products/commodities-and-energy> API
functions. See <https://github.com/risktoollib/RTL>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
