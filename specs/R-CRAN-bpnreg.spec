%global __brp_check_rpaths %{nil}
%global packname  bpnreg
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Projected Normal Regression Models for Circular Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-CRAN-haven >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.1.2.0
Requires:         R-methods >= 3.6.0
Requires:         R-CRAN-haven >= 2.1.1
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Fitting Bayesian multiple and mixed-effect regression models for circular
data based on the projected normal distribution. Both continuous and
categorical predictors can be included. Sampling from the posterior is
performed via an MCMC algorithm. Posterior descriptives of all parameters,
model fit statistics and Bayes factors for hypothesis tests for inequality
constrained hypotheses are provided. See Cremers, Mulder & Klugkist (2018)
<doi:10.1111/bmsp.12108> and Nuñez-Antonio & Guttiérez-Peña (2014)
<doi:10.1016/j.csda.2012.07.025>.

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
