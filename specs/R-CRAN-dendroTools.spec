%global __brp_check_rpaths %{nil}
%global packname  dendroTools
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Methods for Analyzing Daily and Monthly Dendroclimatological Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-psych >= 1.8.3.3
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-dplR >= 1.7.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-boot >= 1.3.22
BuildRequires:    R-CRAN-oce >= 1.2.0
BuildRequires:    R-CRAN-knitr >= 1.19
BuildRequires:    R-CRAN-MLmetrics >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-brnn >= 0.6
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-CRAN-Cubist >= 0.2.2
BuildRequires:    R-stats 
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-psych >= 1.8.3.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-dplR >= 1.7.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-boot >= 1.3.22
Requires:         R-CRAN-oce >= 1.2.0
Requires:         R-CRAN-knitr >= 1.19
Requires:         R-CRAN-MLmetrics >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-brnn >= 0.6
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-Cubist >= 0.2.2
Requires:         R-stats 

%description
Provides novel dendroclimatological methods, primarily used by the
Tree-ring research community. There are four core functions. The first one
is daily_response(), which finds the optimal sequence of days that are
related to one or more tree-ring proxy records. Similar function is
daily_response_seascorr(), which implements partial correlations in the
analysis of daily response functions. For the enthusiast of monthly data,
there is monthly_response() function. The last core function is
compare_methods(), which effectively compares several linear and nonlinear
regression algorithms on the task of climate reconstruction.

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
