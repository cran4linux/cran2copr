%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ameras
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Multiple Exposure Realizations in Association Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MCMCvis 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-stats 
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MCMCvis 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-memoise 
Requires:         R-methods 

%description
Analyze association studies with multiple realizations of a noisy or
uncertain exposure. These can be obtained from e.g. a two-dimensional
Monte Carlo dosimetry system (Simon et al 2015 <doi:10.1667/RR13729.1>) to
characterize exposure uncertainty. The implemented methods are regression
calibration (Carroll et al. 2006 <doi:10.1201/9781420010138>), extended
regression calibration (Little et al. 2023
<doi:10.1038/s41598-023-42283-y>), Monte Carlo maximum likelihood (Stayner
et al. 2007 <doi:10.1667/RR0677.1>), frequentist model averaging (Kwon et
al. 2023 <doi:10.1371/journal.pone.0290498>), and Bayesian model averaging
(Kwon et al. 2016 <doi:10.1002/sim.6635>). Supported model families are
Gaussian, binomial, multinomial, Poisson, proportional hazards, and
conditional logistic.

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
