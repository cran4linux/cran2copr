%global __brp_check_rpaths %{nil}
%global packname  LongDat
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for 'Covariate'-Sensitive Longitudinal Analysis on 'omics' Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-bestNormalize 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-bestNormalize 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-car 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-patchwork 

%description
This tool takes longitudinal dataset as input and analyzes if there is
significant change of the features over time (a proxy for treatments),
while detects and controls for 'covariates' simultaneously. 'LongDat' is
able to take in several data types as input, including count, proportion,
binary, ordinal and continuous data. The output table contains p values,
effect sizes and 'covariates' of each feature, making the downstream
analysis easy.

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
