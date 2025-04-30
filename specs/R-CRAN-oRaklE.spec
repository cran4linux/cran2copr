%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oRaklE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Horizon Electricity Demand Forecasting in High Resolution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-zoo 

%description
Advanced forecasting algorithms for long-term energy demand at the
national or regional level. The methodology is based on Grandón et al.
(2024) <doi:10.1016/j.apenergy.2023.122249>; Zimmermann & Ziel (2024)
<doi:10.2139/ssrn.4823013>. Real-time data, including power demand,
weather conditions, and macroeconomic indicators, are provided through
automated API integration with various institutions. The modular approach
maintains transparency on the various model selection processes and
encompasses the ability to be adapted to individual needs. 'oRaklE' tries
to help facilitating robust decision-making in energy management and
planning.

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
