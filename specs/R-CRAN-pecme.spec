%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pecme
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized ECME Estimation for Censored Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-withr 

%description
Fits Gaussian linear mixed models with a random intercept when the
response is subject to left, right, and/or interval censoring, using the
Expectation/Conditional Maximization Either (ECME) algorithm of Liu and
Rubin (1994) in the spirit of the fast censored-response mixed-model
algorithm of Vaida and Liu (2009). Simultaneous estimation and variable
selection is supported through coordinate-descent penalized maximization
with Lasso, Adaptive Lasso, SCAD, MCP, Elastic Net, and Ridge penalties
(no penalty is also supported). The random intercept is integrated out by
Gauss-Hermite quadrature at every iteration, and the two ECME
conditional-maximization steps respectively maximize the expected
penalized complete-data objective (for the regression coefficients) and
the actual observed-data marginal likelihood (for the variance
components), which is the defining feature of ECME relative to plain
ECM/EM. The package provides a single-fit engine, a sequential/parallel
penalty-parameter grid search with information-criterion or
cross-validated selection, data-dependent or user-supplied lambda grids,
and an Expectation-Maximization based treatment of a completely missing
(at random) response, sharing the same truncated-normal machinery used for
censoring. References: Liu and Rubin (1994) "The ECME algorithm: A simple
extension of EM and ECM with faster monotone convergence"
<doi:10.1093/biomet/81.4.633>; Vaida and Liu (2009) "Fast Implementation
for Normal Mixed Effects Models With Censored Response"
<doi:10.1198/jcgs.2009.07130>.

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
