%global __brp_check_rpaths %{nil}
%global packname  idem
%global packver   5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Inference in Randomized Controlled Trials with Death and Missingness

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-mice >= 3.9.0
BuildRequires:    R-parallel >= 3.2
BuildRequires:    R-CRAN-survival >= 2.38
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-sqldf >= 0.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-mice >= 3.9.0
Requires:         R-parallel >= 3.2
Requires:         R-CRAN-survival >= 2.38
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-sqldf >= 0.4
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
In randomized studies involving severely ill patients, functional outcomes
are often unobserved due to missed clinic visits, premature withdrawal or
death. It is well known that if these unobserved functional outcomes are
not handled properly, biased treatment comparisons can be produced. In
this package, we implement a procedure for comparing treatments that is
based on the composite endpoint of both the functional outcome and
survival. The procedure was proposed in Wang et al. (2016)
<DOI:10.1111/biom.12594> and Wang et al. (2020)
<DOI:10.18637/jss.v093.i12>. It considers missing data imputation with
different sensitivity analysis strategies to handle the unobserved
functional outcomes not due to death.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
