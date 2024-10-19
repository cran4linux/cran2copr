%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BMA
%global packver   3.18.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.18.19
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model Averaging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-rrcov 
Requires:         R-methods 

%description
Package for Bayesian model averaging and variable selection for linear
models, generalized linear models and survival models (cox regression).

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
