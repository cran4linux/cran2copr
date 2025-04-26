%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalModels
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference Modeling for Estimation of Causal Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-causaldata 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-geepack 
Requires:         R-stats 
Requires:         R-CRAN-causaldata 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-geepack 

%description
Provides an array of statistical models common in causal inference such as
standardization, IP weighting, propensity matching, outcome regression,
and doubly-robust estimators. Estimates of the average treatment effects
from each model are given with the standard error and a 95%% Wald
confidence interval (Hernan, Robins (2020)
<https://miguelhernan.org/whatifbook/>).

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
