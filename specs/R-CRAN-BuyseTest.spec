%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BuyseTest
%global packver   3.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Pairwise Comparisons

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-lava 
Requires:         R-parallel 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 

%description
Implementation of the Generalized Pairwise Comparisons (GPC) as defined in
Buyse (2010) <doi:10.1002/sim.3923> for complete observations, and
extended in Peron (2018) <doi:10.1177/0962280216658320> to deal with
right-censoring. GPC compare two groups of observations (intervention vs.
control group) regarding several prioritized endpoints to estimate the
probability that a random observation drawn from one group performs
better/worse/equivalently than a random observation drawn from the other
group. Summary statistics such as the net treatment benefit, win ratio, or
win odds are then deduced from these probabilities. Confidence intervals
and p-values are obtained based on asymptotic results (Ozenne 2021
<doi:10.1177/09622802211037067>), non-parametric bootstrap, or
permutations. The software enables the use of thresholds of minimal
importance difference, stratification, non-prioritized endpoints (O Brien
test), and can handle right-censoring and competing-risks.

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
