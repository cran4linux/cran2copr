%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  copulaSQM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Copula Based Stochastic Frontier Quantile Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ald 
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ald 
Requires:         R-CRAN-VineCopula 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 

%description
Provides estimation procedures for copula-based stochastic frontier
quantile models for cross-sectional data. The package implements maximum
likelihood estimation of quantile regression models allowing flexible
dependence structures between error components through various copula
families (e.g., Gaussian and Student-t). It enables estimation of
conditional quantile effects, dependence parameters, log-likelihood
values, and information criteria (AIC and BIC). The framework combines
quantile regression methodology introduced by Koenker and Bassett (1978)
<doi:10.2307/1913643> with copula theory described in Joe (2014,
ISBN:9781466583221). This approach allows modeling heterogeneous effects
across quantiles while capturing nonlinear dependence structures between
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
