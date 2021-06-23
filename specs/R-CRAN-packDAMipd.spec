%global __brp_check_rpaths %{nil}
%global packname  packDAMipd
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Decision Analysis Modelling Package with Parameters Estimation Ability from Individual Patient Level Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-SurvRegCensCov 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-IPDFileCheck 
BuildRequires:    R-CRAN-valueEQ5D 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-gvlma 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-relaimpo 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-haven 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-SurvRegCensCov 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-IPDFileCheck 
Requires:         R-CRAN-valueEQ5D 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-gvlma 
Requires:         R-methods 
Requires:         R-CRAN-relaimpo 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-haven 

%description
A collection of functions to construct Markov model for model-based
cost-effectiveness analysis. This includes creating Markov model (both
time homogenous and time dependent models), decision analysis, sensitivity
analysis (deterministic and probabilistic). The package allows estimation
of parameters for the Markov model from a given individual patient level
data, provided the data file follows some standard data entry rules.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
