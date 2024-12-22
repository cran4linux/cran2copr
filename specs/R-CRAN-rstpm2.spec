%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rstpm2
%global packver   1.6.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Smooth Survival Models, Including Generalized Survival Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-bbmle >= 1.0.20
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bbmle >= 1.0.20
Requires:         R-CRAN-Rcpp >= 0.10.2
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-mvtnorm 

%description
R implementation of generalized survival models (GSMs), smooth accelerated
failure time (AFT) models and Markov multi-state models. For the GSMs,
g(S(t|x))=eta(t,x) for a link function g, survival S at time t with
covariates x and a linear predictor eta(t,x). The main assumption is that
the time effect(s) are smooth <doi:10.1177/0962280216664760>. For fully
parametric models with natural splines, this re-implements Stata's 'stpm2'
function, which are flexible parametric survival models developed by
Royston and colleagues. We have extended the parametric models to include
any smooth parametric smoothers for time. We have also extended the model
to include any smooth penalized smoothers from the 'mgcv' package, using
penalized likelihood. These models include left truncation, right
censoring, interval censoring, gamma frailties and normal random effects
<doi:10.1002/sim.7451>, and copulas. For the smooth AFTs, S(t|x) =
S_0(t*eta(t,x)), where the baseline survival function
S_0(t)=exp(-exp(eta_0(t))) is modelled for natural splines for eta_0, and
the time-dependent cumulative acceleration factor eta(t,x)=int_0^t
exp(eta_1(u,x)) du for log acceleration factor eta_1(u,x). The Markov
multi-state models allow for a range of models with smooth transitions to
predict transition probabilities, length of stay, utilities and costs,
with differences, ratios and standardisation.

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
