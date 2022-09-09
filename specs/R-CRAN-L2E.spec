%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  L2E
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Structured Regression via the L2 Criterion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-isotone 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-isotone 
Requires:         R-CRAN-cobs 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-robustbase 

%description
An implementation of a computational framework for performing robust
structured regression with the L2 criterion from Chi and Chi (2021+).
Improvements using the majorization-minimization (MM) principle from Liu,
Chi, and Lange (2022+) added in Version 2.0.

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
