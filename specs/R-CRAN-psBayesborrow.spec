%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psBayesborrow
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Information Borrowing with Propensity Score Matching

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-optmatch 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-overlapping 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-optmatch 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-overlapping 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Hybrid control design is a way to borrow information from external
controls to augment concurrent controls in a randomized controlled trial
and is expected to overcome the feasibility issue when adequate randomized
controlled trials cannot be conducted. A major challenge in the hybrid
control design is its inability to eliminate a prior-data conflict caused
by systematic imbalances in measured or unmeasured confounding factors
between patients in the concurrent treatment/control group and external
controls. To prevent the prior-data conflict, a combined use of propensity
score matching and Bayesian commensurate prior has been proposed in the
context of hybrid control design. The propensity score matching is first
performed to guarantee the balance in baseline characteristics, and then
the Bayesian commensurate prior is constructed while discounting the
information based on the similarity in outcomes between the concurrent and
external controls. 'psBayesborrow' is a package to implement the
propensity score matching and the Bayesian analysis with commensurate
prior, as well as to conduct a simulation study to assess operating
characteristics of the hybrid control design, where users can choose
design parameters in flexible and straightforward ways depending on their
own application.

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
