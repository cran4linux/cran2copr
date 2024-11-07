%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ProbBreed
%global packver   1.0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Probability Theory for Selecting Candidates in Plant Breeding

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-rstan >= 2.32.0
BuildRequires:    R-CRAN-StanHeaders >= 2.32.0
BuildRequires:    R-CRAN-BH >= 1.72.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-rstan >= 2.32.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
Use probability theory under the Bayesian framework for calculating the
risk of selecting candidates in a multi-environment context. Contained are
functions used to fit a Bayesian multi-environment model (based on the
available presets), extract posterior values and maximum posterior values,
compute the variance components, check the model’s convergence, and
calculate the probabilities. For both across and within-environments
scopes, the package computes the probability of superior performance and
the pairwise probability of superior performance. Furthermore, the
probability of superior stability and the pairwise probability of superior
stability across environments is estimated. A joint probability of
superior performance and stability is also provided.

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
