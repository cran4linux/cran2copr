%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  httpuv
%global packver   1.6.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.16
Release:          1%{?dist}%{?buildtag}
Summary:          HTTP and WebSocket Server Library

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-later >= 0.8.0
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-later >= 0.8.0
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-utils 

%description
Provides low-level socket and protocol support for handling HTTP and
WebSocket requests directly from within R. It is primarily intended as a
building block for other packages, rather than making it particularly easy
to create complete web applications using httpuv alone.  httpuv is built
on top of the libuv and http-parser C libraries, both of which were
developed by Joyent, Inc. (See LICENSE file for libuv and http-parser
license information.)

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
