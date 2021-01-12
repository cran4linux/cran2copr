%global packname  SAMTx
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Assessment to Unmeasured Confounding with Multiple Treatments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BART 
Requires:         R-CRAN-BART 

%description
A sensitivity analysis approach for unmeasured confounding in
observational data with multiple treatments and a binary outcome. This
approach derives the general bias formula and provides adjusted causal
effect estimates in response to various assumptions about the degree of
unmeasured confounding. Nested multiple imputation is embedded within the
Bayesian framework to integrate uncertainty about the sensitivity
parameters and sampling variability.  Bayesian Additive Regression Model
(BART) is used for outcome modeling. The causal estimands are the average
treatment effects (ATE) based on the risk difference.  For more details,
see paper: Hu L et al. (2020) A flexible sensitivity analysis approach for
unmeasured confounding with a multiple treatments and a binary outcome
<arXiv:2012.06093>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
