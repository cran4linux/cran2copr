%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  landmaRk
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Time-to-Event Landmark Analysis using an Array of Longitudinal and Survival Sub-Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lcmm >= 2.2.2
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-prodlim 
Requires:         R-CRAN-lcmm >= 2.2.2
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-utils 
Requires:         R-CRAN-prodlim 

%description
Provides a modular end-to-end framework for dynamic risk prediction based
on time-to-event and longitudinal data. This allows flexible
specifications for the longitudinal and survival sub-models. The
'landmaRk' package enables reproducible benchmarks of different model
choices, including cross-validation to assess out-of-sample predictive
performance. Methods are described in Velasco-Pardo, Constantine-Cooke,
Lees and Vallejos (2026, manuscript under preparation) 'Landmarking with
Latent Class Mixed Models for Dynamic Prediction of Time-to-event Data
with Heterogeneous Biomarker Trajectories'.

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
