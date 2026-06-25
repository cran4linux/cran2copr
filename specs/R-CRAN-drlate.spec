%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drlate
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Doubly Robust Estimation of Local Average Treatment Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 

%description
Estimates the local average treatment effect (LATE) and the local average
treatment effect on the treated (LATT) using observational data with a
binary instrument, implementing the complete estimator suite of
Sloczynski, Uysal, and Wooldridge: the doubly robust estimators of
Sloczynski, Uysal, and Wooldridge (2022) <doi:10.48550/arXiv.2208.01300>
-- inverse probability weighted regression adjustment (IPWRA), inverse
probability weighting (IPW), augmented inverse probability weighting
(AIPW), and regression adjustment (RA) -- and the Abadie-kappa weighting
estimators of Sloczynski, Uysal, and Wooldridge (2025)
<doi:10.1080/07350015.2024.2332763>. Supports linear, logistic, probit,
Poisson, and fractional (fractional-logit and fractional-probit) outcome
and treatment models, and instrument propensity scores estimated by
maximum likelihood, covariate balancing (CBPS), or inverse probability
tilting (IPT). Standard errors are computed jointly for all estimation
stages by stacking the moment conditions of every model into a single
M-estimation system; weak-instrument-robust Fieller confidence sets,
cluster-aware bootstrap inference, design diagnostics, and a doubly robust
Hausman-type test of unconfoundedness are included. Estimates and standard
errors are validated against the authors' Stata commands 'drlate'
(Statistical Software Components S459708) and 'kappalate' (S459257).

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
