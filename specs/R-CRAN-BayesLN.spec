%global __brp_check_rpaths %{nil}
%global packname  BayesLN
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Log-Normal Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-fAsianOptions 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-fAsianOptions 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Bayesian inference under log-normality assumption must be performed very
carefully. In fact, under the common priors for the variance, useful
quantities in the original data scale (like mean and quantiles) do not
have posterior moments that are finite (Fabrizi et al. 2012
<doi:10.1214/12-BA733>). This package allows to easily carry out a proper
Bayesian inferential procedure by fixing a suitable distribution (the
generalized inverse Gaussian) as prior for the variance. Functions to
estimate several kind of means (unconditional, conditional and conditional
under a mixed model) and quantiles (unconditional and conditional) are
provided.

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
