%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  debiasedTrialEmulation
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pipeline for Debiased Target Trial Emulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-cobalt 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-geex 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ParallelLogger 
BuildRequires:    R-CRAN-EmpiricalCalibration 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-cobalt 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-geex 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ParallelLogger 
Requires:         R-CRAN-EmpiricalCalibration 
Requires:         R-CRAN-purrr 

%description
Supports propensity score-based methods—including matching,
stratification, and weighting—for estimating causal treatment effects. It
also implements calibration using negative control outcomes to enhance
robustness. 'debiasedTrialEmulation' facilitates effect estimation for
both binary and time-to-event outcomes, supporting risk ratio (RR), odds
ratio (OR), and hazard ratio (HR) as effect measures. It integrates
statistical modeling and visualization tools to assess covariate balance,
equipoise, and bias calibration. Additional methods—including approaches
to address immortal time bias, information bias, selection bias, and
informative censoring—are under development. Users interested in these
extended features are encouraged to contact the package authors.

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
