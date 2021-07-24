%global __brp_check_rpaths %{nil}
%global packname  ctsem
%global packver   3.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Time Structural Equation Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0
BuildRequires:    R-CRAN-rstan >= 2.21
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-cOde 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mize 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.21
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-cOde 
Requires:         R-CRAN-expm 
Requires:         R-datasets 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mize 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rstantools

%description
Hierarchical continuous (and discrete) time state space modelling, for
linear and nonlinear systems measured by continuous variables, with
limited support for binary data. The subject specific dynamic system is
modelled as a stochastic differential equation (SDE) or difference
equation, measurement models are typically multivariate normal factor
models. Linear mixed effects SDE's estimated via maximum likelihood and
optimization are the default. Nonlinearities, (state dependent parameters)
and random effects on all parameters are possible, using either max
likelihood / max a posteriori optimization (with optional importance
sampling) or Stan's Hamiltonian Monte Carlo sampling. See
<https://github.com/cdriveraus/ctsem/raw/master/vignettes/hierarchicalmanual.pdf>
for details. Priors may be used. For the conceptual overview of the
hierarchical Bayesian linear SDE approach, see
<https://www.researchgate.net/publication/324093594_Hierarchical_Bayesian_Continuous_Time_Dynamic_Modeling>.
Exogenous inputs may also be included, for an overview of such
possibilities see
<https://www.researchgate.net/publication/328221807_Understanding_the_Time_Course_of_Interventions_with_Continuous_Time_Dynamic_Models>
. Stan based functions are not available on 32 bit Windows systems at
present. <https://cdriver.netlify.app/> contains some tutorial blog posts.

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
