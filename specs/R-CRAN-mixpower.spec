%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixpower
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Power Analysis for Mixed-Effects Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-CRAN-lme4 

%description
A comprehensive, simulation-based toolkit for power and sample-size
analysis for linear and generalized linear mixed-effects models (LMMs and
GLMMs). Supports Gaussian, binomial, Poisson, and negative binomial
families via 'lme4'; Wald and likelihood-ratio tests; multi-parameter
sensitivity grids; power curves and minimum sample-size solvers; parallel
evaluation with deterministic seeds; and full reproducibility (manifests,
result bundling, and export to CSV/JSON). Delivers thorough diagnostics
per run (failure rate, singular-fit rate, effective N) and
publication-ready summary tables. References: Bates et al. (2015) "Fitting
Linear Mixed-Effects Models Using lme4" <doi:10.18637/jss.v067.i01>; Green
and MacLeod (2016) "SIMR: an R package for power analysis of generalized
linear mixed models by simulation" <doi:10.1111/2041-210X.12504>.

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
