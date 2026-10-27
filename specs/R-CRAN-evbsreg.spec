%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evbsreg
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Local Influence Diagnostics for the Extreme-Value Birnbaum-Saunders Regression Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 

%description
Local influence diagnostics for the Extreme-Value Birnbaum-Saunders (EVBS)
regression model of Ferreira, Gomes and Leiva (2012): joint maximum
likelihood estimation, conformal normal curvature diagnostics under
case-weight, response and explanatory-variable perturbation, randomized
quantile residuals with simulation envelope, the density, distribution and
quantile functions, the finite upper endpoint, return levels and expected
shortfall, moving-block bootstrap standard errors, a prospective index of
endpoint identifiability, the same diagnostics for generalized
extreme-value regression, and a 'gamlss' family allowing the tail-shape
parameter to depend on covariates. The methods are described in Lima,
Ospina, Barros and Macedo (2025) <doi:10.48550/arXiv.2507.22967> and are
applied to monthly maximum wind gusts from Itajai, Brazil.

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
