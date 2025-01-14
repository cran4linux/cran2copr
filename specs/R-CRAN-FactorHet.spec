%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FactorHet
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Heterogeneous Effects in Factorial Experiments Using Grouping and Sparsity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-mlrMBO 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-lbfgs 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-mlrMBO 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-lbfgs 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Estimates heterogeneous effects in factorial (and conjoint) models. The
methodology employs a Bayesian finite mixture of regularized logistic
regressions, where moderators can affect each observation's probability of
group membership and a sparsity-inducing prior fuses together levels of
each factor while respecting ANOVA-style sum-to-zero constraints.
Goplerud, Imai, and Pashley (2024) <doi:10.48550/ARXIV.2201.01357> provide
further details.

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
