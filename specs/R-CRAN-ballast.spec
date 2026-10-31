%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ballast
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stress-Test a Pre-Specified Mixed Model for Repeated Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mmrm >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-mmrm >= 0.3.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 

%description
Refits one pre-specified mixed model for repeated measures (MMRM) under
families of data and analytic perturbations (covariance structure,
degrees-of-freedom method and variance estimator, covariate set, analysis
population, alternative analysis data sets, leave-one-out deletions,
crossed specification grids, re-randomisation tests, delta-adjusted and
reference-based multiple imputation, and alternative estimators) and
judges every refit against the pre-specified estimate, confidence interval
and p-value. Classifies the result as robust, sensitive or fragile, with a
separate flag for marginal significance, and estimates by simulation the
probability that a planned design gives a significant and robust result.
Fitting uses 'mmrm' (Sabanes Bove et al., 2024,
<https://openpharma.github.io/mmrm/>) with 'SAS' 'PROC MIXED' conventions
for the least-squares-mean contrast, Kenward-Roger adjustment and the
corrected Akaike criterion. Reference-based multiple imputation follows
Carpenter, Roger and Kenward (2013) <doi:10.1080/10543406.2013.834911> and
was checked against 'rbmi' (Gower-Page, Noci and Wolbers, 2022)
<doi:10.21105/joss.04251>.

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
