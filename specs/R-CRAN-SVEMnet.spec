%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SVEMnet
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Validated Ensemble Models with Lasso and Relaxed Elastic Net Regression

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.1.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet >= 4.1.6
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-utils 

%description
Tools for fitting self-validated ensemble models (SVEM; Lemkus et al.
(2021) <doi:10.1016/j.chemolab.2021.104439>) in small-sample
design-of-experiments and related workflows, using elastic net and relaxed
elastic net regression via 'glmnet' (Friedman et al. (2010)
<doi:10.18637/jss.v033.i01>). Fractional random-weight bootstraps with
anti-correlated validation copies are used to tune penalty paths by
validation-weighted AIC/BIC. Supports Gaussian and binomial responses,
deterministic expansion helpers for shared factor spaces, prediction with
bootstrap uncertainty, and a random-search optimizer that respects mixture
constraints and combines multiple responses via desirability functions.
Also includes a permutation-based whole-model test for Gaussian SVEM fits
(Karl (2024) <doi:10.1016/j.chemolab.2024.105122>). Package code was
drafted with assistance from generative AI tools.

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
