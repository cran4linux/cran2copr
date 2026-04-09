%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CEDMr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Capability-Ecological Developmental Model (CEDM) Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 6.7.0
BuildRequires:    R-CRAN-mediation >= 4.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-lme4 >= 1.1.31
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-stats 
Requires:         R-CRAN-rms >= 6.7.0
Requires:         R-CRAN-mediation >= 4.5.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-lme4 >= 1.1.31
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-stats 

%description
Implements the Capability-Ecological Developmental Model (CEDM) for
longitudinal and multilevel data. The package supports estimation and
interpretation of models examining how socioeconomic status (SES), health
indicators, and contextual factors jointly relate to academic outcomes.
Functionality includes: (1) classification of ecological capability
regimes (amplifying, neutral, compensatory); (2) estimation of moderated
multilevel models with higher-order interaction terms; (3) causal
mediation analysis using doubly robust estimation; (4) random-effects
within-between (REWB) decomposition; (5) nonlinear moderation using
restricted cubic splines; (6) clustering of longitudinal health
trajectories; and (7) sensitivity analysis using the impact threshold for
a confounding variable (ITCV) and robustness-to-replacement (RIR)
measures. The package is designed for use with general longitudinal
multilevel datasets.

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
