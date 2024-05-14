%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remstimate
%global packver   2.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Optimization Frameworks for Tie-Oriented and Actor-Oriented Relational Event Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-remify >= 3.2.4
BuildRequires:    R-CRAN-remstats >= 3.2.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-remify >= 3.2.4
Requires:         R-CRAN-remstats >= 3.2.1
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-mvnfast 

%description
A comprehensive set of tools designed for optimizing likelihood within a
tie-oriented (Butts, C., 2008, <doi:10.1111/j.1467-9531.2008.00203.x>) or
an actor-oriented modelling framework (Stadtfeld, C., & Block, P., 2017,
<doi:10.15195/v4.a14>) in relational event networks. The package
accommodates both frequentist and Bayesian approaches. The frequentist
approaches that the package incorporates are the Maximum Likelihood
Optimization (MLE) and the Gradient-based Optimization (GDADAMAX). The
Bayesian methodologies included in the package are the Bayesian Sampling
Importance Resampling (BSIR) and the Hamiltonian Monte Carlo (HMC). The
flexibility of choosing between frequentist and Bayesian optimization
approaches allows researchers to select the estimation approach which
aligns the most with their analytical preferences.

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
