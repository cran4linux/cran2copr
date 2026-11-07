%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiExposure
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exposure-Lag-Response Modeling for Plant Disease Epidemiology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-spaMM 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-dlnm 
Requires:         R-stats 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-spaMM 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Supports modeling and interpretation of environmental
exposure-lag-response relationships in plant disease epidemiology using
distributed lag non-linear models (DLNMs). Provides functions for defining
complete exposure profiles, evaluating model identifiability, summarizing
lag-specific and period-specific effects, performing sensitivity analyses,
simulating environmental exposure scenarios, predicting plant disease
outcomes, quantifying yield and economic losses, and evaluating individual
and ensemble models. Supports harmonized frequentist and Bayesian modeling
workflows. Builds on the framework implemented in the 'dlnm' package and
described by Gasparrini (2011) <doi:10.18637/jss.v043.i08>.

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
