%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exhaustiveRasch
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Item Selection and Exhaustive Search for Rasch Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eRm 
BuildRequires:    R-CRAN-psychotree 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-pairwise 
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-eRm 
Requires:         R-CRAN-psychotree 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-tictoc 
Requires:         R-methods 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-pairwise 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-pbapply 

%description
Automation of the item selection processes for Rasch scales by means of
exhaustive search for suitable Rasch models (dichotomous, partial credit,
rating-scale) in a list of item-combinations. The item-combinations to
test can be either all possible combinations or item-combinations can be
defined by several rules (forced inclusion of specific items, exclusion of
combinations, minimum/maximum items of a subset of items). Tests for model
fit and item fit include ordering of the thresholds, item fit-indices,
likelihood ratio test, Martin-Löf test, Wald-like test, person-item
distribution, person separation index, principal components of Rasch
residuals, empirical representation of all raw scores or Rasch trees for
detecting differential item functioning. The tests, their ordering and
their parameters can be defined by the user. For parameter estimation and
model tests, functions of the packages 'eRm', 'psychotools' or 'pairwise'
can be used.

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
