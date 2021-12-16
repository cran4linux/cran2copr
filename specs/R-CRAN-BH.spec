%global __brp_check_rpaths %{nil}
%global packname  BH
%global packver   1.78.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.78.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Boost C++ Header Files

License:          BSL-1.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Boost provides free peer-reviewed portable C++ source libraries.  A large
part of Boost is provided as C++ template code which is resolved entirely
at compile-time without linking.  This package aims to provide the most
useful subset of Boost libraries for template use among CRAN packages. By
placing these libraries in this package, we offer a more efficient
distribution system for CRAN as replication of this code in the sources of
other packages is avoided. As of release 1.78.0-0, the following Boost
libraries are included: 'accumulators' 'algorithm' 'align' 'any' 'atomic'
'beast' 'bimap' 'bind' 'circular_buffer' 'compute' 'concept' 'config'
'container' 'date_time' 'detail' 'dynamic_bitset' 'exception' 'flyweight'
'foreach' 'functional' 'fusion' 'geometry' 'graph' 'heap' 'icl' 'integer'
'interprocess' 'intrusive' 'io' 'iostreams' 'iterator' 'lambda2' 'math'
'move' 'mp11' 'mpl' 'multiprecision' 'numeric' 'pending' 'phoenix'
'polygon' 'preprocessor' 'process' 'propery_tree' 'random' 'range'
'scope_exit' 'smart_ptr' 'sort' 'spirit' 'tuple' 'type_traits' 'typeof'
'unordered' 'utility' 'uuid'.

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
