%global __brp_check_rpaths %{nil}
%global packname  VGAMextra
%global packver   0.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Additions and Extensions of the 'VGAM' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-VGAM >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
Requires:         R-CRAN-VGAM >= 1.1.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-stats4 

%description
Extending the functionalities of the 'VGAM' package with additional
functions and datasets. At present, 'VGAMextra' comprises new family
functions (ffs) to estimate several time series models by maximum
likelihood using Fisher scoring, unlike popular packages in CRAN relying
on optim(), including ARMA-GARCH-like models, the Order-(p, d, q) ARIMAX
model (non- seasonal), the Order-(p) VAR model, error correction models
for cointegrated time series, and ARMA-structures with Student-t errors.
For independent data, new ffs to estimate the inverse- Weibull, the
inverse-gamma, the generalized beta of the second kind and the general
multivariate normal distributions are available. In addition, 'VGAMextra'
incorporates new VGLM-links for the mean-function, and the
quantile-function (as an alternative to ordinary quantile modelling) of
several 1-parameter distributions, that are compatible with the class of
VGLM/VGAM family functions. Currently, only fixed-effects models are
implemented. All functions are subject to change; see the NEWS for further
details on the latest changes.

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
