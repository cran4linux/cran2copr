%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSReliabilityClaytonMWD
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stress-Strength Reliability Model with MWD Marginals via Clayton Copula

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-knitr 
Requires:         R-stats 

%description
Implements stress-strength reliability models under a dependent framework,
where both stress and strength variables follow modified Weibull
distributions and their dependence is modeled using a Clayton copula
(Kizilaslan (2026) <doi:10.48550/arXiv.2604.12130>). The package provides
several estimation procedures for model parameters and the stress-strength
reliability R, including two-step maximum likelihood estimation (MLE),
least squares estimation (LSE), weighted least squares estimation (WLSE),
and maximum product of spacings (MPS). It also provides interval
estimation using asymptotic confidence intervals based on MLE and
bootstrap confidence intervals for all methods. In addition, functions are
included for parameter estimation of the modified Weibull distribution
(Lai et al. (2003) <doi:10.1109/TR.2002.805788>) and the two-parameter
Weibull distribution, along with utilities to compute their probability
density function, cumulative distribution function, quantile function, and
to generate random samples.

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
