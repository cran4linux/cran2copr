%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dendroTools
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Methods for Analyzing Daily and Monthly Dendroclimatological Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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
Provides methods for analyzing the relationships between tree-ring proxies
and daily or monthly climate data. daily_response() and monthly_response()
aggregate climate data over moving windows of different widths and
positions, optionally extending into previous years. For each window, they
calculate the correlation (Pearson, Spearman or Kendall) with a proxy, or
the explained variance of linear models or Bayesian regularized neural
networks with one or more proxies, and find the window with the strongest
relationship. daily_response_seascorr() and monthly_response_seascorr()
calculate partial correlations between a proxy and a primary climate
variable, controlling for a second one, following 'seascorr' by Meko et
al. (2011) <doi:10.1016/j.cageo.2011.01.013>. They also partition the
variance explained in the optimal window between the two variables and can
calculate the partial correlations of the second variable. The climate
data in each window can be aggregated as means, sums and other statistics,
or as the Standardized Precipitation-Evapotranspiration Index (SPEI) by
Vicente-Serrano et al. (2010) <doi:10.1175/2009JCLI2909.1>, calculated
from the climatic water balance that water_balance() derives from
precipitation and temperature. The aggregated climate series can be
detrended linearly or with the spline, mean, autoregressive and Friedman
methods of dplR::detrend(). Windows that are not significant can be
removed with a per-window test or with corrections for multiple testing.
Bootstrap confidence intervals are available, and the optimal window can
be checked for temporal stability and by cross-validation.
compare_methods() compares multiple linear regression, neural networks,
model trees and random forests for climate reconstruction. The methods are
described in Jevsenak and Levanic (2018)
<doi:10.1016/j.dendro.2018.01.005>, Jevsenak et al. (2018)
<doi:10.1016/j.dendro.2018.10.001> and Jevsenak (2020)
<doi:10.1016/j.dendro.2020.125753>.

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
