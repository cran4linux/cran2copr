%global packname  digest
%global packver   0.6.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.25
Release:          3%{?dist}%{?buildtag}
Summary:          Create Compact Hash Digests of R Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Implementation of a function 'digest()' for the creation of hash digests
of arbitrary R objects (using the 'md5', 'sha-1', 'sha-256', 'crc32',
'xxhash', 'murmurhash' and 'spookyhash' algorithms) permitting easy
comparison of R language objects, as well as functions such as'hmac()' to
create hash-based message authentication code. Please note that this
package is not meant to be deployed for cryptographic purposes for which
more comprehensive (and widely tested) libraries such as 'OpenSSL' should
be used.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/GPL-2
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
