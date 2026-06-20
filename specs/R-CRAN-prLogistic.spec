%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prLogistic
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Prevalence Ratios via Logistic Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-graphics 

%description
Estimates adjusted prevalence ratios (PR) and their confidence intervals
from logistic regression models, addressing the well-known limitation of
odds ratios (OR) as approximations to PR in cross-sectional studies with
common outcomes. Supports independent observations (glm()),
clustered/multilevel data (glmer() from 'lme4'), longitudinal data via
Generalised Estimating Equations (geeglm() from 'geepack'), and complex
survey designs (svyglm() from 'survey'). Inference is available via the
delta method (conditional and marginal standardisation) and via bootstrap
(normal-approximation and percentile intervals). Continuous covariates are
handled through user-specified or median-based reference values; flexible
baseline specification allows any reference category to be chosen for
factor predictors. Based on the methodology described in Amorim & Ospina
(2021) <doi:10.1590/0001-3765202120190316>.

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
