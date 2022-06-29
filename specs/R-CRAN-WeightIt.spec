%global __brp_check_rpaths %{nil}
%global packname  WeightIt
%global packver   0.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weighting for Covariate Balance in Observational Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cobalt >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-backports >= 1.4.1
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-cobalt >= 4.3.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-backports >= 1.4.1
Requires:         R-CRAN-crayon 

%description
Generates balancing weights for causal effect estimation in observational
studies with binary, multi-category, or continuous point or longitudinal
treatments by easing and extending the functionality of several R packages
and providing in-house estimation methods. Available methods include
propensity score weighting using generalized linear models, gradient
boosting machines, the covariate balancing propensity score algorithm,
Bayesian additive regression trees, and SuperLearner, and directly
estimating balancing weights using entropy balancing, empirical balancing
calibration weights, energy balancing, and optimization-based weights.
Also allows for assessment of weights and checking of covariate balance by
interfacing directly with the 'cobalt' package. See the vignette
"Installing Supporting Packages" for instructions on how to install any
package 'WeightIt' uses, including those that may not be on CRAN.

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
