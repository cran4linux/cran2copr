%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesqm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Q Methodology: Probabilistic Factor Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstantools >= 2.3.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-parallel 
Requires:         R-CRAN-rstantools >= 2.3.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-parallel 

%description
A Bayesian factor-analytic framework for Q methodology. Fits a low-rank
factor model to Q-sort data with a Student-t likelihood and a hierarchical
normal prior on loadings, samples the posterior with Stan, resolves
rotational ambiguity via the MatchAlign post-processing of Poworoznek et
al. (2025) <doi:10.1214/25-BA1544>, and returns posterior summaries
including credible intervals for loadings and factor scores, probabilistic
dominant-factor membership, distinguishing and consensus statements, and
PSIS-LOO-based factor enumeration following Vehtari et al. (2017)
<doi:10.1007/s11222-016-9696-4> with the Sivula et al. (2025)
<doi:10.1214/25-BA1569> parsimony rule.

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
