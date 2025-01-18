%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lrstat
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size Calculation for Non-Proportional Hazards and Beyond

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-lpSolve >= 5.6.1
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-lpSolve >= 5.6.1
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-Rcpp >= 1.0.9

%description
Performs power and sample size calculation for non-proportional hazards
model using the Fleming-Harrington family of weighted log-rank tests. The
sequentially calculated log-rank test score statistics are assumed to have
independent increments as characterized in Anastasios A. Tsiatis (1982)
<doi:10.1080/01621459.1982.10477898>. The mean and variance of log-rank
test score statistics are calculated based on Kaifeng Lu (2021)
<doi:10.1002/pst.2069>. The boundary crossing probabilities are calculated
using the recursive integration algorithm described in Christopher
Jennison and Bruce W. Turnbull (2000, ISBN:0849303168). The package can
also be used for continuous, binary, and count data. For continuous data,
it can handle missing data through mixed-model for repeated measures
(MMRM). In crossover designs, it can estimate direct treatment effects
while accounting for carryover effects. For binary data, it can design
Simon's 2-stage, modified toxicity probability-2 (mTPI-2), and Bayesian
optimal interval (BOIN) trials. For count data, it can design group
sequential trials for negative binomial endpoints with censoring.
Additionally, it facilitates group sequential equivalence trials for all
supported data types. Moreover, it can design adaptive group sequential
trials for changes in sample size, error spending function, number and
spacing or future looks. Finally, it offers various options for adjusted
p-values, including graphical and gatekeeping procedures.

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
