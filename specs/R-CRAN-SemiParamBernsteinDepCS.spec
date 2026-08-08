%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SemiParamBernsteinDepCS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Bayesian Regression for Dependent Current Status Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements a semiparametric Bayesian regression framework using Bernstein
polynomial baseline models for analyzing dependent current status data.
The package accommodates proportional hazards (PH) and proportional odds
(PO) regression models with Archimedean copulas ('Gumbel', 'Frank', and
'Clayton') to model the joint dependence structure between event and
observation or censoring times. Estimation is performed using a Robust
Adaptive Metropolis (RAM) Markov Chain Monte Carlo ('MCMC') algorithm.
Model comparison metrics including Deviance Information Criterion ('DIC')
and posterior summaries with Highest Posterior Density ('HPD') intervals
and Kendall's tau are provided. Methodological details are described in
Sharma and Balakrishnan (2026) <doi:10.1080/02664763.2026.2701921>.

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
