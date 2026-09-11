%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stratifyR
%global packver   2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Stratification of Univariate Populations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr >= 2.0.0
BuildRequires:    R-CRAN-fitdistrplus >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-mc2d 
Requires:         R-CRAN-nloptr >= 2.0.0
Requires:         R-CRAN-fitdistrplus >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-mc2d 

%description
Determines Optimum Strata Boundaries (OSB) and Optimum Sample Sizes (OSS)
for univariate stratified sampling designs under Neyman allocation.  The
stratification variable is described by a best-fitting parametric
distribution, selected automatically by AIC from a set of continuous
families (normal, log-normal, gamma, Weibull, exponential, Cauchy,
uniform, Pareto, triangular and right-triangular), and the optimum
boundaries are obtained by minimising the Neyman objective. Version 2.0
keeps the original globally optimal Dynamic Programming (DP) solver of
Reddy and Khan (2020) as the default and adds two faster derivative-free
alternatives for interactive and large-scale use: a multi-start 'COBYLA'
solver and a two-phase 'global' solver that couples 'DIRECT-L' with
'COBYLA' refinement.  It also provides cost-constrained allocation with
unequal per-stratum costs, a design-efficiency comparison
(compare_designs), two- and three-dimensional and interactive
visualisations, solution-quality diagnostics (a Cauchy-Schwarz optimality
gap and KKT first-order residuals for the derivative-free solvers) and a
self-contained 'shiny' application, while remaining backward compatible
with the strata.data() and strata.distr() interface of version 1.x.  The
methodology follows Khan et al. (2008)
<https://www150.statcan.gc.ca/n1/pub/12-001-x/2008002/article/10761-eng.pdf>,
Reddy and Khan (2018) <doi:10.1111/anzs.12244> and Reddy and Khan (2020)
<doi:10.1111/anzs.12301>.

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
