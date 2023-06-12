%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sanitizers
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          C/C++ Source Code to Trigger Address and Undefined Behaviour Sanitizers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Recent gcc and clang compiler versions provide functionality to test for
memory violations and other undefined behaviour; this is often referred to
as "Address Sanitizer" (or 'ASAN') and "Undefined Behaviour Sanitizer"
('UBSAN'). The Writing R Extension manual describes this in some detail in
Section 4.3 title "Checking Memory Access".

This feature has to be enabled in the corresponding binary, eg in R, which
is somewhat involved as it also required a current compiler toolchain
which is not yet widely available, or in the case of Windows, not
available at all (via the common Rtools mechanism).

As an alternative, pre-built Docker containers such as the Rocker
container 'r-devel-san' or the multi-purpose container 'r-debug' can be
used.

This package then provides a means of testing the compiler setup as the
known code failures provides in the sample code here should be detected
correctly, whereas a default build of R will let the package pass.

The code samples are based on the examples from the Address Sanitizer Wiki
at <https://github.com/google/sanitizers/wiki>.

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
