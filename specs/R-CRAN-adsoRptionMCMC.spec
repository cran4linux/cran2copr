%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adsoRptionMCMC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Adsorption Isotherms via MCMC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides tools for Bayesian parameter estimation of adsorption isotherm
models using Markov Chain Monte Carlo (MCMC) methods. This package enables
users to fit non-linear and linear adsorption isotherm models—Freundlich,
Langmuir, and Temkin—within a probabilistic framework, capturing
uncertainty and parameter correlations. It provides posterior summaries,
95%% credible intervals, convergence diagnostics (Gelman-Rubin), and
visualizations through trace and density plots. With this R package,
researchers can rigorously analyze adsorption behavior in environmental
and chemical systems using robust Bayesian inference. For more details,
see Gilks et al. (1995) <doi:10.1201/b14835>, and Gamerman & Lopes (2006)
<doi:10.1201/9781482296426>.

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
