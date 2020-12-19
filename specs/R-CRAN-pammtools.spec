%global packname  pammtools
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Piece-Wise Exponential Additive Mixed Modeling Tools for Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.2
BuildRequires:    R-CRAN-survival >= 2.39.5
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pec 
Requires:         R-CRAN-ggplot2 >= 3.2.2
Requires:         R-CRAN-survival >= 2.39.5
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pec 

%description
The Piece-wise exponential (Additive Mixed) Model (PAMM; Bender and
Scheipl (2018) <doi: 10.1177/1471082X17748083>) is a powerful model class
for the analysis of survival (or time-to-event) data, based on Generalized
Additive (Mixed) Models (GA(M)Ms). It offers intuitive specification and
robust estimation of complex survival models with stratified baseline
hazards, random effects, time-varying effects, time-dependent covariates
and cumulative effects (Bender and others (2018) <doi:
10.1093/biostatistics/kxy003>, as well as support for left-truncated,
competing risks and recurrent events data. pammtools provides tidy
workflow for survival analysis with PAMMs, including data simulation,
transformation and other functions for data preprocessing and model
post-processing as well as visualization.

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
