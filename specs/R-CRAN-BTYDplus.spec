%global __brp_check_rpaths %{nil}
%global packname  BTYDplus
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Models for Assessing and Predicting your Customer Base

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-BTYD >= 2.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-BTYD >= 2.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-bayesm 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides advanced statistical methods to describe and predict customers'
purchase behavior in a non-contractual setting. It uses historic
transaction records to fit a probabilistic model, which then allows to
compute quantities of managerial interest on a cohort- as well as on a
customer level (Customer Lifetime Value, Customer Equity, P(alive), etc.).
This package complements the BTYD package by providing several additional
buy-till-you-die models, that have been published in the marketing
literature, but whose implementation are complex and non-trivial. These
models are: NBD [Ehrenberg (1959) <doi:10.2307/2985810>], MBG/NBD
[Batislam et al (2007) <doi:10.1016/j.ijresmar.2006.12.005>], (M)BG/CNBD-k
[Reutterer et al (2020) <doi:10.1016/j.ijresmar.2020.09.002>], Pareto/NBD
(HB) [Abe (2009) <doi:10.1287/mksc.1090.0502>] and Pareto/GGG [Platzer and
Reutterer (2016) <doi:10.1287/mksc.2015.0963>].

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
