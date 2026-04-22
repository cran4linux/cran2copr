%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GARCH.X
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Exogenous Covariate Selection for ARCH-m(X), Additive ARCH-m(x), and GARCH-X Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-KernSmooth 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-nnls 
Requires:         R-utils 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-KernSmooth 

%description
Estimates the parameters and nonparametric functions of an ARCH-m(X) model
with exogenous covariates, estimates the parameters and nonparametric
functions of an Additive ARCH-m(X) model with exogenous covariates,
estimates the parameters of a GARCH-X model with exogenous covariates,
performs hypothesis tests for the covariates returning the p-values, and
performs stepwise variable selection on the exogenous covariates, and uses
False Discovery Rate p-value corrections to select the exogenous
variables.

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
