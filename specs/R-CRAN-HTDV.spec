%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HTDV
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Testing for Dependent Variables with Unbalanced Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-rstantools

%description
Implements hierarchical Bayesian inference, robust frequentist inference,
and distribution-free inference for dependent and unbalanced data under
strong-mixing conditions. Supports triangular-array, weighted-sum and
mixingale convergence regimes with Whittle and composite likelihoods,
heteroskedasticity-and-autocorrelation-consistent variance estimation,
block bootstrap with automatic block length, fixed-bandwidth HAR
inference, adaptive conformal prediction, Bayesian decision under Region
of Practical Equivalence, bridge-sampling Bayes factors, and predictive
comparison via the Widely Applicable Information Criterion and
leave-future-out cross-validation. Methods follow Andrews (1991)
<doi:10.2307/2938229>, Kiefer and Vogelsang (2005)
<doi:10.1017/S0266466605050565>, Patton, Politis and White (2009)
<doi:10.1080/07474930802459016>, Vehtari, Gelman and Gabry (2017)
<doi:10.1007/s11222-016-9696-4>, Kruschke (2018)
<doi:10.1177/2515245918771304>, and Gibbs and Candes (2021)
<doi:10.48550/arXiv.2106.00170>.

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
