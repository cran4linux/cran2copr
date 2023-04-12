%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pwrss
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Power and Sample Size Calculation Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Statistical power and minimum required sample size calculations for (1)
testing a proportion (one-sample) against a constant, (2) testing a mean
(one-sample) against a constant, (3) testing difference between two
proportions (independent samples), (4) testing difference between two
means or groups (parametric and non-parametric tests for independent and
paired samples), (5) testing a correlation (one-sample) against a
constant, (6) testing difference between two correlations (independent
samples), (7) testing a single coefficient in multiple linear regression,
logistic regression, and Poisson regression (with standardized or
unstandardized coefficients, with no covariates or covariate adjusted),
(8) testing an indirect effect (with standardized or unstandardized
coefficients, with no covariates or covariate adjusted) in the mediation
analysis (Sobel, Joint, and Monte Carlo tests), (9) testing an R-squared
against zero in linear regression, (10) testing an R-squared difference
against zero in hierarchical regression, (11) testing an eta-squared or
f-squared (for main and interaction effects) against zero in analysis of
variance (could be one-way, two-way, and three-way), (12) testing an
eta-squared or f-squared (for main and interaction effects) against zero
in analysis of covariance (could be one-way, two-way, and three-way), (13)
testing an eta-squared or f-squared (for between, within, and interaction
effects) against zero in one-way repeated measures analysis of variance
(with non-sphericity correction and repeated measures correlation), and
(14) testing goodness-of-fit or independence for contingency tables.
Alternative hypothesis can be formulated as "not equal", "less",
"greater", "non-inferior", "superior", or "equivalent" in (1), (2), (3),
and (4); as "not equal", "less", or "greater" in (5), (6), (7) and (8);
but always as "greater" in (9), (10), (11), (12), (13), and (14).
Reference: Bulus and Polat (2023) <https://osf.io/ua5fc>.

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
