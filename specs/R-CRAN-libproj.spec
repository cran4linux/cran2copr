%global __brp_check_rpaths %{nil}
%global packname  libproj
%global packver   8.1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generic Coordinate Transformation Library ('PROJ') C API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-rappdirs 

%description
Provides a 'PROJ' <https://proj.org> C API that can be used to write
high-performance C and C++ coordinate transformation operations using R as
an interface. This package contains an internal version of the 'PROJ'
library to guarantee the best possible consistency on multiple platforms,
and to provide a means by which 'PROJ' can be used on platforms where it
may be impractical or impossible to install a binary version of the
library.

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
