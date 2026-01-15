%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesDiagnostics
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Bayesian Model Diagnostics and Comparison Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-loo >= 2.5.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-brms >= 2.18.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-posterior >= 1.0.0
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-loo >= 2.5.0
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-brms >= 2.18.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-posterior >= 1.0.0
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-rstantools

%description
Provides comprehensive tools for Bayesian model diagnostics and
comparison. Includes prior sensitivity analysis, posterior predictive
checks (Gelman et al. (2013) <doi:10.1201/b16018>), advanced model
comparison using Pareto-smoothed importance sampling leave-one-out
cross-validation (Vehtari et al. (2017) <doi:10.1007/s11222-016-9696-4>),
convergence diagnostics, and prior elicitation tools. Integrates with
'brms' (Burkner (2017) <doi:10.18637/jss.v080.i01>), 'rstan', and
'rstanarm' packages for comprehensive Bayesian workflow diagnostics.

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
