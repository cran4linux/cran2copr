%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparseSEM
%global packver   3.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Elastic Net Penalized Maximum Likelihood for Structural Equation Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
Provides elastic net regularized maximum likelihood for structural
equation models (SEM) in inferring network structure (topology) and
estimating causal effects. The package implements `lasso` and `elastic
net` (l1/l2) penalized SEM and estimates the model parameters with an
efficient block coordinate ascent algorithm that maximizes the penalized
likelihood of the SEM.  Hyperparameters are inferred from cross-validation
(CV).  A Stability Selection (STS) function is also available to provide
accurate causal effect selection.

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
