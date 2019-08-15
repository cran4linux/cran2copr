%global packname  BH
%global packver   1.69.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.69.0.1
Release:          1%{?dist}
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
useful subset of Boost libraries for template use among CRAN package. By
placing these libraries in this package, we offer a more efficient
distribution system for CRAN as replication of this code in the sources of
other packages is avoided. As of release 1.69.0-1, the following Boost
libraries are included: 'algorithm' 'align' 'any' 'atomic' 'bimap' 'bind'
'circular_buffer' 'compute' 'concept' 'config' 'container' 'date_time'
'detail' 'dynamic_bitset' 'exception' 'filesystem' 'flyweight' 'foreach'
'functional' 'fusion' 'geometry' 'graph' 'heap' 'icl' 'integer'
'interprocess' 'intrusive' 'io' 'iostreams' 'iterator' 'math' 'move' 'mpl'
'multiprcecision' 'numeric' 'pending' 'phoenix' 'preprocessor'
'propery_tree' 'random' 'range' 'scope_exit' 'smart_ptr' 'sort' 'spirit'
'tuple' 'type_traits' 'typeof' 'unordered' 'utility' 'uuid'.

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
