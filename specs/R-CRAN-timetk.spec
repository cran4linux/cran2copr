%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timetk
%global packver   2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool Kit for Working with Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-zoo >= 1.7.14
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-stringi >= 1.4.6
BuildRequires:    R-CRAN-readr >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-recipes >= 1.0.4
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-padr >= 0.5.2
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-slider 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tsfeatures 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-zoo >= 1.7.14
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-stringi >= 1.4.6
Requires:         R-CRAN-readr >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-recipes >= 1.0.4
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-padr >= 0.5.2
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-slider 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tsfeatures 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-generics 

%description
Easy visualization, wrangling, and feature engineering of time series data
for forecasting and machine learning prediction. Consolidates and extends
time series functionality from packages including 'dplyr', 'stats', 'xts',
'forecast', 'slider', 'padr', 'recipes', and 'rsample'.

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
