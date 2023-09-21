%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoxAIPW
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Doubly Robust Inference for Cox Marginal Structural Model with Informative Censoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-gbm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-gbm 

%description
Doubly robust estimation and inference of log hazard ratio under the Cox
marginal structural model with informative censoring. An augmented inverse
probability weighted estimator that involves 3 working models, one for
conditional failure time T, one for conditional censoring time C and one
for propensity score. Both models for T and C can depend on both a binary
treatment A and additional baseline covariates Z, while the propensity
score model only depends on Z. With the help of cross-fitting techniques,
achieves the rate-doubly robust property that allows the use of most
machine learning or non-parametric methods for all 3 working models, which
are not permitted in classic inverse probability weighting or doubly
robust estimators. When the proportional hazard assumption is violated,
CoxAIPW estimates a causal estimated that is a weighted average of the
time-varying log hazard ratio. Reference: Luo, J. (2023). Statistical
Robustness - Distributed Linear Regression, Informative Censoring, Causal
Inference, and Non-Proportional Hazards [Unpublished doctoral
dissertation]. University of California San Diego.; Luo & Xu (2022)
<doi:10.48550/arXiv.2206.02296>; Rava (2021)
<https://escholarship.org/uc/item/8h1846gs>.

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
