%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  budgetIVr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Identification of Causal Effects with Mostly Invalid Instruments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rglpk 
Requires:         R-stats 

%description
A tuneable and interpretable method for relaxing the instrumental
variables (IV) assumptions to infer treatment effects in the presence of
unobserved confounding. For a treatment-associated covariate to be a valid
IV, it must be (a) unconfounded with the outcome and (b) have a causal
effect on the outcome that is exclusively mediated by the exposure. There
is no general test of the validity of these IV assumptions for any
particular pre-treatment covariate. However, if different pre-treatment
covariates give differing causal effect estimates when treated as IVs,
then we know at least some of the covariates violate these assumptions.
'budgetIVr' exploits this fact by taking as input a minimum budget of
pre-treatment covariates assumed to be valid IVs and idenfiying the set of
causal effects that are consistent with the user's data and budget
assumption. The following generalizations of this principle can be used in
this package: (1) a vector of multiple budgets can be assigned alongside
corresponding thresholds that model degrees of IV invalidity; (2) budgets
and thresholds can be chosen using specialist knowledge or varied in a
principled sensitivity analysis; (3) treatment effects can be nonlinear
and/or depend on multiple exposures (at a computational cost). The methods
in this package require only summary statistics. Confidence sets are
constructed under the "no measurement error" (NOME) assumption from the
Mendelian randomization literature. For further methodological details,
please refer to Penn et al. (2024) <doi:10.48550/arXiv.2411.06913>.

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
