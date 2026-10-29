%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAmeasures
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Performance Assessment for Continuous and Survival Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pmcalibration >= 0.2.0
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tdROC 
BuildRequires:    R-CRAN-survivalROC 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-prodlim 
Requires:         R-CRAN-pmcalibration >= 0.2.0
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tdROC 
Requires:         R-CRAN-survivalROC 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-prodlim 

%description
Evaluates prediction accuracy for continuous outcomes and the predictive
performance of survival models in a unified framework. Implements the
R-squared, L-squared, pseudo R-squared and related explained variation
measures of Li and Wang (2019) <doi:10.1080/01621459.2018.1515079>, the
concordance indices of Harrell et al. (1982)
<doi:10.1001/jama.1982.03320430047030> and Uno et al. (2011)
<doi:10.1002/sim.4154>, the time-dependent area under the receiver
operating characteristic curve (AUC) of Heagerty, Lumley and Pepe (2000)
<doi:10.1111/j.0006-341X.2000.00337.x>, and the Brier score of Graf et al.
(1999)
<doi:10.1002/(SICI)1097-0258(19990915/30)18:17/18%%3C2529::AID-SIM274%%3E3.0.CO;2-5>.
Supports right-censored data; competing risks, following Wolbers et al.
(2014) <doi:10.1093/biostatistics/kxt059>, Wu and Li (2018)
<doi:10.1002/sim.7806> and Zhuang et al. (2025)
<doi:10.48550/arXiv.2507.15040>; and two-phase sampling designs such as
case-cohort and nested case-control studies, following Lee,
Zeleniuch-Jacquotte and Liu (2021) <doi:10.1080/02664763.2020.1861225>.
Revives and expands the original 'PAmeasures' package with a unified
interface for survival prediction assessment.

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
