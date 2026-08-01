%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BetaDanish
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Beta-Danish Distribution for Lifetime Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-grDevices 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-tools 

%description
Implements the four-parameter Beta-Danish distribution and its
three-parameter Exponentiated Danish submodel for survival, reliability
and lifetime data analysis, following Ahmad and Danish (2025)
<doi:10.2478/jamsi-2025-0010>. Density, distribution, quantile, survival,
hazard and random generation functions are evaluated so as to retain
accuracy in the heavy upper tail, where the survival function is regularly
varying. Estimation covers maximum likelihood for complete and
right-censored samples, ridge-penalized fitting for weakly identified
regimes, a grouped likelihood for times recorded on a coarse grid, and
Bayesian sampling. Inference provides log-scale Wald and profile
likelihood intervals, together with a reparameterization in terms of the
identified composite of the two shape parameters. Structural properties
include raw, incomplete and conditional moments with their existence
conditions, Shannon, Renyi and Tsallis entropies, mean residual life, mean
deviations, Lorenz and Bonferroni curves, probability weighted moments,
order statistics, stress-strength reliability, hazard shape classification
and the tail index. Regression modules cover accelerated failure time
models, mixture and promotion-time cure models, and competing risks with
Aalen-Johansen comparison and Gray's test. Analyses can be run directly
from a delimited text file or spreadsheet.

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
