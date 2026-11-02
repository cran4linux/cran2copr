%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Gtheory4LLM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalizability Theory for LLM Subjective Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildRequires:    R-CRAN-OpenMx >= 2.22.11
BuildRequires:    R-CRAN-Matrix >= 1.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-OpenMx >= 2.22.11
Requires:         R-CRAN-Matrix >= 1.6.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Studies the reliability and generalizability of subjective judgments
produced by large language models (LLMs), including annotation, rating,
and structured LLM-as-a-judge tasks. Specifies evaluator, prompt,
generation, and repeated-run facets through crossed or explicitly nested
random sources with configurable item interactions. Fits univariate
models, joint Gaussian models, and joint discrete models for binary,
ordinal, and unordered categorical outcomes, with source-specific
covariance. Gaussian models use exact balanced likelihood, with a bounded
observed-row route for incomplete univariate panels. Discrete models use
dense or sparse first-order Laplace approximation with Gaussian latent
random effects. Supported balanced decision studies compare evaluator,
prompt, and replication allocations using observed Gaussian or explicitly
requested latent binary and ordinal reliability, with random or fixed
facets after Brennan (2001). 'OpenMx' Gaussian fits report asymptotic Wald
standard errors for variance components and delta-method coefficient
intervals when curvature checks permit them; the 'lme4' route returns
point estimates only. Discrete fits offer optional full-information latent
coefficient intervals, subject to numerical and boundary checks. An object
bootstrap refits resampled objects under each fit's acceptance rule and
gives percentile and bias-corrected and accelerated intervals for
components, coefficients and decision studies. Provides fixed-layout call
effects, categorical score and category-vector reliability projections,
repeated-panel decision agreement, bounded cost-aware comparisons, and
Gaussian or latent binary/ordinal pilot precision planning, and
categorical point-estimator pilot operating characteristics. Joint
Gaussian-discrete fitting is not implemented. Includes three publicly
archived LLM annotation datasets covering hate-speech, mental-health, and
drug-review tasks. Discrete fitting retains conservative size limits; the
preflight report describes supported designs and computational limits.
Generalizability coefficients follow the variance-decomposition framework
of Brennan (2001) <doi:10.1007/978-1-4757-3456-0>.

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
