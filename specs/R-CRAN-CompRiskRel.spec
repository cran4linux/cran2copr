%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompRiskRel
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reliability and Competing Risks Analysis under Hybrid Censoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Generalized computational algorithms for competing risks analysis,
stress-strength reliability modeling, optimal designs, and reliability
acceptance sampling plans under various hybrid censoring schemes. Includes
data generation routines, Maximum Likelihood Estimation (MLE) with seven
optimization algorithms ('Newton-Raphson', 'BFGS', 'BFGSR', 'BHHH',
'SANN', 'CG', and 'Nelder-Mead'), Bayesian inference via Gibbs sampling
and Metropolis-Hastings MCMC, Importance Sampling, and 'Lindley'
asymptotic approximation. Visualization functions generate histograms, dot
plots, and autocorrelation plots for model validation. Methodology and
design principles are based on 'Balakrishnan', 'Cramer', and 'Kundu'
(2023, "Hybrid Censoring Know-How: Designs and Implementations", Academic
Press, ISBN:978-0-12-398387-9).

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
