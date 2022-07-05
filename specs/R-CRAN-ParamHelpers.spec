%global __brp_check_rpaths %{nil}
%global packname  ParamHelpers
%global packver   1.14.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14.1
Release:          1%{?dist}%{?buildtag}
Summary:          Helpers for Parameters in Black-Box Optimization, Tuning and Machine Learning

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-BBmisc >= 1.10
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-methods 
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-BBmisc >= 1.10
Requires:         R-CRAN-backports 
Requires:         R-CRAN-fastmatch 
Requires:         R-methods 

%description
Functions for parameter descriptions and operations in black-box
optimization, tuning and machine learning. Parameters can be described
(type, constraints, defaults, etc.), combined to parameter sets and can in
general be programmed on. A useful OptPath object (archive) to log
function evaluations is also provided.

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
