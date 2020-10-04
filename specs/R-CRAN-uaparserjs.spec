%global packname  uaparserjs
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          Parse 'User-Agent' Strings

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-V8 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-V8 

%description
Despite there being a section in RFC 7231
<https://tools.ietf.org/html/rfc7231#section-5.5.3> defining a suggested
structure for 'User-Agent' headers this data is notoriously difficult to
parse consistently. Tools are provided that will take in user agent
strings and return structured R objects. This is a 'V8'-backed package
based on the 'ua-parser' project <https://github.com/ua-parser>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/extdat
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
