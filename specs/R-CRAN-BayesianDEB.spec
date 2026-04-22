%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianDEB
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Dynamic Energy Budget Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-posterior >= 1.5.0
BuildRequires:    R-CRAN-deSolve >= 1.40
BuildRequires:    R-CRAN-bayesplot >= 1.10.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-posterior >= 1.5.0
Requires:         R-CRAN-deSolve >= 1.40
Requires:         R-CRAN-bayesplot >= 1.10.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a Bayesian framework for Dynamic Energy Budget (DEB) modelling
via 'Stan'. Implements the standard DEB model of Kooijman (2010,
<doi:10.1017/CBO9780511805400>) as a state-space model with Hamiltonian
Monte Carlo inference (Carpenter et al., 2017,
<doi:10.18637/jss.v076.i01>). Includes individual-level growth models,
growth-reproduction models, hierarchical multi-individual models with
partial pooling, and toxicokinetic-toxicodynamic (TKTD) models for
ecotoxicology following the DEBtox framework (Jager et al., 2006,
<doi:10.1007/s10646-006-0060-x>). Supports prior specification from
biological knowledge, convergence diagnostics (Vehtari et al., 2021,
<doi:10.1214/20-BA1221>), posterior predictive checks, derived quantity
estimation, and visualisation via 'ggplot2'.

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
