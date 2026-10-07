%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scorecraft
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scorecard Development and Internal Ratings-Based Risk Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-OptimalBinningWoE >= 1.13.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-OptimalBinningWoE >= 1.13.4
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-xgboost 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Builds points scorecards for binary targets (credit risk, fraud,
propensity) on the optimal binning and weight of evidence engine of
'OptimalBinningWoE', and takes them to the risk parameters of the internal
ratings-based (IRB) approach. Variables are selected through optimal
binning, eight admission rules, hold-out revalidation with frozen bins and
a consensus of 'glmnet', 'xgboost', 'lightgbm' and 'ranger' models
weighted by out-of-sample performance; the audit funnel never drops a
candidate from the report. The scorecard is fitted with an explicit,
auditable scale alignment (a log-odds regression on the raw score composed
with the points-to-double-the-odds map); cut-offs are swept with frozen
cuts; reject inference is reported as a sensitivity band; the population
and characteristic stability indices (PSI and CSI) are monitored with both
the fixed and the sample-size-adjusted threshold; and production SQL is
generated in fourteen dialects, with the agreement between R and SQL
verified by test. The IRB layer builds the default flag; calibrates the
scorecard to a long-run default rate with rating grades, margins of
conservatism and floors to give the probability of default (PD); models
workout loss given default (LGD) in two stages with downturn and
in-default estimates; models credit conversion factors from facility
snapshots to give the exposure at default (EAD); and computes expected
loss, risk weights, regulatory capital and expected credit loss from
parameter tables selected by framework preset. The heavy numeric kernels
(rank correlation of wide weight of evidence tables, exact concordance
counts for Somers' D, streamed expected credit loss paths) are compiled
with 'RcppArmadillo'. The scorecard methodology follows Siddiqi (2017)
<doi:10.1002/9781119282396> and Thomas et al. (2017)
<doi:10.1137/1.9781611974560>.

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
