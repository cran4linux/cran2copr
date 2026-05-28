%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastSurvival
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Kaplan-Meier, Log-Rank, and Hazard Ratio Estimation for Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-Rcpp 

%description
Provides fast alternatives to standard survival analysis functions in the
'survival' package. The package implements a single-time-point
Kaplan-Meier estimator (survfit_fast()), a log-rank test
(survdiff_fast()), a closed-form hazard ratio estimator based on the
Pike-Halley Estimator method (coxph_fast()), and a clinical trial data
simulator (simdata_fast()). All functions are designed for repeated
evaluation inside large simulation loops, such as adaptive sample-size
re-estimation, probability-of-success calculations, and regional
consistency evaluation in multi-regional trials. Core computations are
implemented in 'C++' via 'Rcpp' for maximum performance. Methodological
background is described in Collett (2014, ISBN:9780429196294).

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
