%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdyncall
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Improved Foreign Function Interface and Dynamic Bindings to C Libraries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
Provides a cross-platform framework for dynamic binding of C libraries
using a flexible Foreign Function Interface (FFI). The FFI supports almost
all fundamental C types, multiple calling conventions, symbolic access to
foreign C struct/union data types and wrapping of R functions as C
callback function pointers. Dynamic bindings to shared C libraries are
data-driven by cross-platform binding specifications using a compact plain
text format; the package includes a 'DynPort' binding specification for
'SDL3' generated from current headers with 'porter'. The package includes
a variety of technology demos and OS-specific notes for installation of
shared libraries. For the underlying methods and bundled 'DynCall'
libraries, see Adler (2012) <doi:10.32614/RJ-2012-004> and Adler and
Philipp (2008) <https://dyncall.org>.

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
