%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OLStrajr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ordinary Least Squares Trajectory Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
The 'OLStrajr' package provides comprehensive functions for ordinary least
squares (OLS) trajectory analysis and case-by-case OLS regression as
outlined in Carrig, Wirth, and Curran (2004)
<doi:10.1207/S15328007SEM1101_9> and Rogosa and Saner (1995)
<doi:10.3102/10769986020002149>. It encompasses two primary functions,
OLStraj() and cbc_lm(). The OLStraj() function simplifies the estimation
of individual growth curves over time via OLS regression, with options for
visualizing both group-level and individual-level growth trajectories and
support for linear and quadratic models. The cbc_lm() function facilitates
case-by-case OLS estimates and provides unbiased mean population intercept
and slope estimators by averaging OLS intercepts and slopes across cases.
It further offers standard error calculations across bootstrap replicates
and computation of 95%% confidence intervals based on empirical
distributions from the resampling processes.

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
