%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3fselect
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-bbotk >= 1.0.0
BuildRequires:    R-CRAN-paradox >= 1.0.0
BuildRequires:    R-CRAN-mlr3misc >= 0.15.1
BuildRequires:    R-CRAN-mlr3 >= 0.12.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stabm 
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-bbotk >= 1.0.0
Requires:         R-CRAN-paradox >= 1.0.0
Requires:         R-CRAN-mlr3misc >= 0.15.1
Requires:         R-CRAN-mlr3 >= 0.12.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stabm 

%description
Feature selection package of the 'mlr3' ecosystem. It selects the optimal
feature set for any 'mlr3' learner. The package works with several
optimization algorithms e.g. Random Search, Recursive Feature Elimination,
and Genetic Search. Moreover, it can automatically optimize learners and
estimate the performance of optimized feature sets with nested resampling.

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
