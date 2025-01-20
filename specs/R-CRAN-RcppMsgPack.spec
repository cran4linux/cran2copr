%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppMsgPack
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          'MsgPack' C++ Header Files and Interface Functions for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 

%description
'MsgPack' header files are provided for use by R packages, along with the
ability to access, create and alter 'MsgPack' objects directly from R.
'MsgPack' is an efficient binary serialization format. It lets you
exchange data among multiple languages like 'JSON' but it is faster and
smaller. Small integers are encoded into a single byte, and typical short
strings require only one extra byte in addition to the strings themselves.
This package provides headers from the 'msgpack-c' implementation for C
and C++(11) for use by R, particularly 'Rcpp'. The included 'msgpack-c'
headers are licensed under the Boost Software License (Version 1.0); the
code added by this package as well the R integration are licensed under
the GPL (>= 2). See the files 'COPYRIGHTS' and 'AUTHORS' for a full list
of copyright holders and contributors to 'msgpack-c'.

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
