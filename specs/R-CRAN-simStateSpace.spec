%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simStateSpace
%global packver   1.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.15
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Data from State Space Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 15.0.2.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-stats 

%description
Provides a streamlined and user-friendly framework for simulating data in
state space models, particularly when the number of subjects/units (n)
exceeds one, a scenario commonly encountered in social and behavioral
sciences. This package was designed to generate data for the simulations
performed in Pesigan, Russell, and Chow (2025) <doi:10.1037/met0000779>.

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
