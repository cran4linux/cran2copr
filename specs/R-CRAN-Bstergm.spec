%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Bstergm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Separable Temporal Exponential Random Graph Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-ergm >= 4.6.0
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ergm.multi 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-ergm >= 4.6.0
Requires:         R-CRAN-network 
Requires:         R-CRAN-ergm.multi 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
Bayesian inference for separable temporal exponential random graph models
(STERGMs) of dynamic binary networks and for the separable two-layer
STERGMs of dynamic signed networks (Caimo and Gollini, 2026). Each
transition is decomposed into the formation and persistence of ties (and,
for signed networks, of their signs); the resulting doubly-intractable
posteriors are sampled with approximate exchange algorithms based on
adaptive Metropolis-Hastings or adaptive direction sampling. Posterior
predictive goodness of fit, diagnostics of the auxiliary simulations,
simulation and forecasting tools are provided.

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
