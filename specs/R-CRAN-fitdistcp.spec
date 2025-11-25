%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitdistcp
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Distribution Fitting with Calibrating Priors for Commonly Used Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mev 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-gnorm 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rust 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-fExtremes 
Requires:         R-stats 
Requires:         R-CRAN-mev 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-gnorm 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rust 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-fExtremes 

%description
Generates predictive distributions based on calibrating priors for various
commonly used statistical models, including models with predictors.
Routines for densities, probabilities, quantiles, random deviates and the
parameter posterior are provided. The predictions are generated from the
Bayesian prediction integral, with priors chosen to give good reliability
(also known as calibration). For homogeneous models, the prior is set to
the right Haar prior, giving predictions which are exactly reliable. As a
result, in repeated testing, the frequencies of out-of-sample outcomes and
the probabilities from the predictions agree. For other models, the prior
is chosen to give good reliability. Where possible, the Bayesian
prediction integral is solved exactly. Where exact solutions are not
possible, the Bayesian prediction integral is solved using the
Datta-Mukerjee-Ghosh-Sweeting (DMGS) asymptotic expansion. Optionally, the
prediction integral can also be solved using posterior samples generated
using Paul Northrop's ratio of uniforms sampling package ('rust'). Results
are also generated based on maximum likelihood, for comparison purposes.
Various model selection diagnostics and testing routines are included.
Based on "Reducing reliability bias in assessments of extreme weather risk
using calibrating priors", Jewson, S., Sweeting, T. and Jewson, L. (2024);
<doi:10.5194/ascmo-11-1-2025>.

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
