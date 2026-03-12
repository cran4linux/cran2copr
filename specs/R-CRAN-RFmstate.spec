%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RFmstate
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forest-Based Multistate Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ranger 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Fits cause-specific random survival forests for flexible multistate
survival analysis with covariate-adjusted transition probabilities
computed via product-integral. State transitions are modeled by random
forests. Subject-specific transition probability matrices are assembled
from predicted cumulative hazards using the product-integral formula. Also
provides a standalone Aalen-Johansen nonparametric estimator as a
covariate-free baseline. Supports arbitrary state spaces with any number
of states (three or more) and any set of allowed transitions, applicable
to clinical trials, disease progression, reliability engineering, and
other domains where subjects move among discrete states over time.
Provides per-transition feature importance, bias-variance diagnostics, and
comprehensive visualizations. Handles right censoring and competing
transitions. Methods are described in Ishwaran et al. (2008)
<doi:10.1214/08-AOAS169> for random survival forests, Putter et al. (2007)
<doi:10.1002/sim.2712> for multistate competing risks decomposition, and
Aalen and Johansen (1978) <https://www.jstor.org/stable/4615704> for the
nonparametric estimator.

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
