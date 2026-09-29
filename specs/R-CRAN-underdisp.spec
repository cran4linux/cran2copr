%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  underdisp
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics and Models for Underdispersed Count Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-VGAM 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 

%description
Tools for detecting and modeling underdispersion in count data
(conditional variance below the conditional mean), the case the Poisson
and negative binomial defaults cannot represent. Provides a screening
diagnostic that benchmarks at-risk dispersion against a zero-truncated
Poisson, regression-adjusted tests of equidispersion, and a dispersion
profile that compares the variance-to-mean curves of competing families
against the data; the continuous parameter binomial (CPB) and generalized
event count (Katz) regressions with zero-truncated, hurdle, and
zero-inflated forms and high-dimensional fixed effects with a split-panel
jackknife bias correction; matched Poisson, negative binomial, COM-Poisson
(rate- and mean-parameterized), generalized Poisson, gamma-count, and
double Poisson regressions through the same interface, with frequency
weights, offsets, and analytic, robust, and cluster-robust standard
errors; bootstrap and profile-likelihood inference; proper scoring rules,
rootograms, PIT histograms, and simulation methods; and quantities of
interest including predicted distributions, the implied ceiling, rate
ratios, and first differences with an extensive/intensive decomposition.
The likelihoods are implemented in C++.

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
