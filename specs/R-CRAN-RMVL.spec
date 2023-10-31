%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMVL
%global packver   0.0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Mappable Vector Library for Handling Large Datasets

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Mappable vector library provides convenient way to access large datasets.
Use all of your data at once, with few limits. Memory mapped data can be
shared between multiple R processes. Access speed depends on storage
medium, so solid state drive is recommended, preferably with PCI Express
(or M.2 nvme) interface or a fast network file system. The data is memory
mapped into R and then accessed using usual R list and array subscription
operators. Convenience functions are provided for merging, grouping and
indexing large vectors and data.frames. The layout of underlying MVL files
is optimized for large datasets. The vectors are stored to guarantee
alignment for vector intrinsics after memory map. The package is built on
top of libMVL, which can be used as a standalone C library. libMVL has
simple C API making it easy to interchange datasets with outside programs.

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
