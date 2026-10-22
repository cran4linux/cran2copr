%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hsquared
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          'R' Interface for 'Julia'-Backed Quantitative-Genetic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 

%description
Provides an interface for quantitative-genetic models in 'R', backed by
the 'HSquared.jl' engine for 'Julia'. Fits Gaussian pedigree animal models
by restricted maximum likelihood, using average-information restricted
maximum likelihood (AI-REML; Gilmour et al. (1995) <doi:10.2307/2533274>)
for the univariate model. Returns heritability, variance components,
breeding values, and covariance and correlation matrices for multivariate
models. Formula and pedigree validation can run without 'Julia'. Model
fitting requires a local 'Julia' and 'HSquared.jl'; use hs_control(engine
= "validate") to preview the model contract without fitting. What you may
report is listed on the package article 'Can I fit and report this?', not
in validation_status(), which is a developer evidence table.
Model-specific restrictions are documented in that article. Uncertainty
intervals are not coverage-calibrated.

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
