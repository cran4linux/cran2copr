%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iPEB
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Improved Parametric Empirical Bayes for Longitudinal Biomarker Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Extends parametric empirical Bayes (PEB) for longitudinal biomarker
screening with a time-gap-aware standardization layer, covariate
adjustment, and objective-driven multi-marker weighting. The layer models
each subject's biomarker history with a random intercept (and an optional
random slope) and autocorrelated, gap-scaled residuals, so that prediction
uncertainty grows with the time between visits and per-visit specificity
is preserved under irregular sampling. Marker weights are learned to
optimize a user-selected clinical objective -- maximizing sensitivity at a
fixed specificity, extending detection lead time, or a combined objective
-- with optional feature selection and a choice of scalar or multivariate
combiner. Functions for fitting, prediction, and evaluation (sensitivity,
lead time, and specificity at chosen operating points) are provided. A
manuscript describing the method is in preparation.

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
