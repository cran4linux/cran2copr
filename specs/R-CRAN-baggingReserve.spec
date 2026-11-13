%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baggingReserve
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bagging and Regression Trees for Individual Claims Reserving

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rngtools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-codetools 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rngtools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Claim-level (individual) loss reserving in non-life insurance, and the
means to check claim-level reserves against the payments that followed. A
data contract turns a table of claims and a table of payment transactions
into a claim-by-development-year panel at a valuation date; a recursion
engine completes the payment history of every reported claim one
development year ahead, with plugged-in means or simulated payments, for
regression trees, their bootstrap aggregation (bagging) and user-supplied
learners; payments for incurred-but-not-reported claims are added from
chain-ladder claim counts and the average predicted payment per
development year; and back-tests score a prediction and a reference method
such as the chain ladder against realised payments by calendar year and
component. The default estimator is the method of Janoušek and Pešta
(2025) <doi:10.1007/s00362-025-01715-9>, one regression tree per
development year with bagging for replicate predictions, whose spread
describes the bootstrap resampling variation of the predictions of (by
default unpruned) trees, and an out-of-bag diagnostic of the one-year
regressions; for totals beyond next year simulated instead of plugged-in
completion is recommended. Ships a reproducible synthetic
individual-claims dataset generated with the individual claims simulator
of Wang and Wüthrich, built on 'SynthETIC'.

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
