%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FBCRM
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phase I Optimal Dose Assignment using the FBCRM and MFBCRM Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Performs dose assignment and trial simulation for the FBCRM (Fully
Bayesian Continual Reassessment Method) and MFBCRM (Mixture Fully Bayesian
Continual Reassessment Method) phase I clinical trial designs. These trial
designs extend the Continual Reassessment Method (CRM) and Bayesian Model
Averaging Continual Reassessment Method (BMA-CRM) by allowing the prior
toxicity skeleton itself to be random, with posterior distributions
obtained from Markov Chain Monte Carlo. On average, the FBCRM and MFBCRM
methods outperformed the CRM and BMA-CRM methods in terms of selecting an
optimal dose level across thousands of randomly generated simulation
scenarios. Details on the methods and results of this simulation study are
available on request, and the manuscript is currently under review.

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
