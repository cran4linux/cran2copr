%global __brp_check_rpaths %{nil}
%global packname  fable.ata
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          'ATAforecasting' Modelling Interface for 'fable' Framework

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fabletools >= 0.3.1
BuildRequires:    R-CRAN-ATAforecasting >= 0.0.56
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-tsbox 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-fabletools >= 0.3.1
Requires:         R-CRAN-ATAforecasting >= 0.0.56
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-tsbox 
Requires:         R-CRAN-lubridate 

%description
Allows ATA (Automatic Time series analysis using the Ata method) models
from the 'ATAforecasting' package to be used in a tidy workflow with the
modeling interface of 'fabletools'. This extends 'ATAforecasting' to
provide enhanced model specification and management, performance
evaluation methods, and model combination tools. The Ata method (Yapar et
al. (2019) <doi:10.15672/hujms.461032>), an alternative to exponential
smoothing (described in Yapar (2016) <doi:10.15672/HJMS.201614320580>,
Yapar et al. (2017) <doi:10.15672/HJMS.2017.493>), is a new univariate
time series forecasting method which provides innovative solutions to
issues faced during the initialization and optimization stages of existing
forecasting methods. Forecasting performance of the Ata method is superior
to existing methods both in terms of easy implementation and accurate
forecasting. It can be applied to non-seasonal or seasonal time series
which can be decomposed into four components (remainder, level, trend and
seasonal).

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
