%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustMediate
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Mediation Analysis with Diagnostics and Sensitivity Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-broom 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-broom 

%description
Provides tools for causal mediation analysis with continuous treatments
using inverse probability weighting (IPW). Estimates natural direct and
indirect effects over a user-defined treatment grid and supports flexible
dose-response mediation analysis. Includes diagnostic procedures for
assessing covariate balance in both treatment and mediator models using
standardized mean differences. Implements pathway-specific extensions of
the impact threshold for a confounding variable (ITCV; Frank, 2000
<doi:10.1177/0049124100029002001>) adapted to mediation settings. Provides
joint sensitivity analysis combining E-values (VanderWeele and Ding, 2017
<doi:10.7326/M16-2607>) and violations of sequential ignorability (Imai,
Keele, and Yamamoto, 2010 <doi:10.1214/10-STS321>). Additional utilities
include visualization of dose-response mediation functions, robustness
profiles, fragility summaries, and formatted outputs for applied research.
Supports clustered data structures and multiple outcome families.

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
