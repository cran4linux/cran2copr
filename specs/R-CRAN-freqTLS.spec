%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  freqTLS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Frequentist Inference for Thermal Load Sensitivity Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-TMB 
Requires:         R-utils 

%description
A maximum-likelihood implementation of the thermal-load-sensitivity
framework for thermal death-time modelling introduced by Noble, Arnold and
Pottier in the 'bayesTLS' package, providing the frequentist counterpart
to that Bayesian workflow. The modelling idea and the four-parameter
logistic parameterisation are theirs; 'freqTLS' contributes a 'Template
Model Builder' ('TMB') likelihood whose midpoint is written directly in
terms of critical thermal maximum ('CTmax') and thermal sensitivity (z) so
both headline quantities are estimable, and reports uncertainty through a
unified trio of frequentist intervals -- Wald (delta), profile-likelihood,
and bootstrap -- for binomial and beta-binomial survival counts and
beta-distributed proportions. Column and formula interfaces support fixed
and grouped designs plus limited independent random intercepts; prediction
includes survival curves and deterministic heat-injury scenarios.
Equivalence claims are restricted to the matched relative-threshold,
constant-shape 'bayesTLS' configuration.

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
