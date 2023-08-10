%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visit
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Vaccine Phase I Design with Simultaneous Evaluation of Immunogenicity and Toxicity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.2
BuildRequires:    R-parallel >= 3.2
BuildRequires:    R-CRAN-rstan >= 2.19.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1.10
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-sqldf >= 0.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.2
Requires:         R-parallel >= 3.2
Requires:         R-CRAN-rstan >= 2.19.2
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-sqldf >= 0.4
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Phase I clinical trials are the first step in drug development to test a
new drug or drug combination on humans. Typical designs of Phase I trials
use toxicity as the primary endpoint and aim to find the maximum tolerable
dosage. However, these designs are poorly applicable for the development
of cancer therapeutic vaccines because the expected safety concerns for
these vaccines are not as much as cytotoxic agents. The primary objectives
of a cancer therapeutic vaccine phase I trial thus often include
determining whether the vaccine shows biologic activity and the minimum
dose necessary to achieve a full immune or even clinical response. This
package implements a Bayesian Phase I cancer vaccine trial design that
allows simultaneous evaluation of safety and immunogenicity outcomes. See
Wang et al. (2019) <DOI:10.1002/sim.8021> for further details.

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
