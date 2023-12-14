%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DFBA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distribution-Free Bayesian Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
A set of functions to perform distribution-free Bayesian analyses.
Included are Bayesian analogues to the frequentist Mann-Whitney U test,
the Wilcoxon Signed-Ranks test, Kendall's Tau Rank Correlation
Coefficient, Goodman and Kruskal's Gamma, McNemar's Test, the binomial
test, the sign test, the median test, as well as distribution-free methods
for testing contrasts among condition and for computing Bayes factors for
hypotheses. The package also includes procedures to estimate the power of
distribution-free Bayesian tests based on data simulations using various
probability models for the data. The set of functions provide data
analysts with a set of Bayesian procedures that avoids requiring
parametric assumptions about measurement error and is robust to problem of
extreme outlier scores.

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
