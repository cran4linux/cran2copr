%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bbotk
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Black-Box Optimization Toolkit

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-paradox >= 1.0.0
BuildRequires:    R-CRAN-mlr3misc >= 0.15.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-paradox >= 1.0.0
Requires:         R-CRAN-mlr3misc >= 0.15.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-methods 
Requires:         R-CRAN-R6 

%description
Features highly configurable search spaces via the 'paradox' package and
optimizes every user-defined objective function. The package includes
several optimization algorithms e.g. Random Search, Iterated Racing,
Bayesian Optimization (in 'mlr3mbo') and Hyperband (in 'mlr3hyperband').
bbotk is the base package of 'mlr3tuning', 'mlr3fselect' and
'miesmuschel'.

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
