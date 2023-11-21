%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3tuning
%global packver   0.19.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.19.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hyperparameter Optimization for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-bbotk >= 0.7.3
BuildRequires:    R-CRAN-mlr3 >= 0.17.0
BuildRequires:    R-CRAN-mlr3misc >= 0.13.0
BuildRequires:    R-CRAN-paradox >= 0.10.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-bbotk >= 0.7.3
Requires:         R-CRAN-mlr3 >= 0.17.0
Requires:         R-CRAN-mlr3misc >= 0.13.0
Requires:         R-CRAN-paradox >= 0.10.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-R6 

%description
Hyperparameter optimization package of the 'mlr3' ecosystem. It features
highly configurable search spaces via the 'paradox' package and finds
optimal hyperparameter configurations for any 'mlr3' learner. 'mlr3tuning'
works with several optimization algorithms e.g. Random Search, Iterated
Racing, Bayesian Optimization (in 'mlr3mbo') and Hyperband (in
'mlr3hyperband'). Moreover, it can automatically optimize learners and
estimate the performance of optimized models with nested resampling.

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
