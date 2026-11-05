%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggchangepoint
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Combines Changepoint Analysis with 'ggplot2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-changepoint.np 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-changepoint.np 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
A unified, tidy, 'ggplot2'-native interface to changepoint detection in R.
A 'cpt_detect()' dispatcher covers 51 methods (penalised and optimal
partitioning, multiscale and search methods, nonparametric and kernel
methods, Bayesian methods, high-dimensional, functional, covariance and
network methods, regression breaks through a formula interface,
seasonal-trend decomposition, the classical single-change tests, and
anomalous stretches that return to a baseline), with distribution families
for counts, binary outcomes and waiting times, missing-value handling,
grouped data, and constraints on locations and segment lengths. Every
result is the same 'ggcpt' object, in one verified location convention,
with 'broom'-style tidy/glance/augment methods, 'autoplot()' and
composable 'ggproto' layers. Around detection: which coordinates of a
multivariate series changed, certified with family-wise error control;
distribution-free confidence sets for each location; effect sizes and what
the series would have done without each change; a test for a change at a
date fixed in advance, tests for a change anywhere, and screening of many
series with false discovery rate control; a check of whether a change was
abrupt or gradual; weights over the number of changes; assumption checks
and goodness of fit, robustness to the noise model, stability, consensus
and influence diagnostics, supervised detection, sequential monitoring
including cumulative-sum and exponentially weighted moving-average control
charts, power and study design, benchmarks, reports and an export under a
documented 'JSON' schema. What each engine does (its runtime, whether its
answer survives a change of units or a reversal of time, its false
positives by noise regime and data type, its false alarms on pure noise)
and the calibration of the package's own intervals, tests and monitors are
measured and shipped as data, and 'cpt_recommend()' chooses from those
measurements. 'cpt_register_method()' brings external and non-CRAN
detectors into the same grammar.

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
