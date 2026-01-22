%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggsced
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities and Helpers for Single Case Experimental Design (SCED) using 'ggplot2'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-assert 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggh4x 
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-assert 

%description
Provides specialized visualization tools for Single-Case Experimental
Design (SCED) research using 'ggplot2'. SCED studies are a crucial
methodology in behavioral and educational research where individual
participants serve as their own controls through carefully designed
experimental phases. This package extends 'ggplot2' to create
publication-ready graphics with professional phase change lines, support
for multiple baseline designs, and styling functions that follow SCED
visualization conventions. Key functions include adding phase change
demarcation lines to existing plots and formatting axes with broken axis
appearance commonly used in single-case research.

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
