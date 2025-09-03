%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trendtestR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Trend Analysis and Visualization for Time-Series and Grouped Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-car 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-rlang 
Requires:         R-splines 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-mgcv 

%description
Provides a set of exploratory data analysis (EDA) tools for visualizing
trends, diagnosing data types for beginner-friendly workflows, and
automatically routing to suitable statistical tests or trend exploration
models. Includes unified plotting functions for trend lines, grouped
boxplots, and comparative scatterplots; automated statistical testing
(e.g., t-test, Wilcoxon, ANOVA, Kruskal-Wallis, Tukey, Dunn) with optional
effect size calculation; and model-based trend analysis using generalized
additive models (GAM) for count data, generalized linear models (GLM) for
continuous data, and zero-inflated models (ZIP/ZINB) for count data with
potential zero-inflation. Also supports time-window continuity checks,
cross-year handling in compare_monthly_cases(), and ARIMA-ready
preparation with stationarity diagnostics, ensuring consistent parameter
styles for reproducible research and user-friendly workflows.Methods are
based on R Core Team (2024) <https://www.R-project.org/>, Wood, S.N.(2017,
ISBN:978-1498728331), Hyndman RJ, Khandakar Y (2008)
<doi:10.18637/jss.v027.i03>, Simon Jackman (2024)
<https://github.com/atahk/pscl/>, Achim Zeileis, Christian Kleiber, Simon
Jackman (2008) <doi:10.18637/jss.v027.i08>.

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
