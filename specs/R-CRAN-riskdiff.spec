%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riskdiff
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Difference Estimation with Multiple Link Functions and Inverse Probability of Treatment Weighting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Calculates risk differences (or prevalence differences for cross-sectional
data) and Number Needed to Treat (NNT) using generalized linear models
with automatic link function selection. Provides robust model fitting with
fallback methods, support for stratification and adjustment variables,
inverse probability of treatment weighting (IPTW) for causal inference
with NNT calculations, and publication-ready output formatting. Handles
model convergence issues gracefully and provides confidence intervals
using multiple approaches. Methods are based on approaches described in
Mark W. Donoghoe and Ian C. Marschner (2018) "logbin: An R Package for
Relative Risk Regression Using the Log-Binomial Model"
<doi:10.18637/jss.v086.i09> for robust GLM fitting, Peter C. Austin (2011)
"An Introduction to Propensity Score Methods for Reducing the Effects of
Confounding in Observational Studies" <doi:10.1080/00273171.2011.568786>
for IPTW methods, and standard epidemiological methods for risk difference
estimation as described in Kenneth J. Rothman, Sander Greenland and
Timothy L. Lash (2008, ISBN:9780781755641) "Modern Epidemiology".

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
