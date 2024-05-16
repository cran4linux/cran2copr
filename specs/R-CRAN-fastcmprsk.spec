%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastcmprsk
%global packver   1.24.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.24.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fine-Gray Regression via Forward-Backward Scan

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-dynpred 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-dynpred 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
In competing risks regression, the proportional subdistribution hazards
(PSH) model is popular for its direct assessment of covariate effects on
the cumulative incidence function. This package allows for both penalized
and unpenalized PSH regression in linear time using a novel
forward-backward scan. Penalties include Ridge, Lease Absolute Shrinkage
and Selection Operator (LASSO), Smoothly Clipped Absolute Deviation
(SCAD), Minimax Concave Plus (MCP), and elastic net <doi:
10.32614/RJ-2021-010>.

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
