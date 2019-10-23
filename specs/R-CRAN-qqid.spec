%global packname  qqid
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Generation and Support of QQIDs - A Human-CompatibleRepresentation of 128-bit Numbers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-qrandom 
Requires:         R-CRAN-qrandom 

%description
The string "bird.carp.7TsBWtwqtKAeCTNk8f" is a "QQID": a representation of
a 128-bit number, constructed from two "cues" of short, common, English
words, and Base64 encoded characters.  The primary intended use of QQIDs
is as random unique identifiers, e.g. database keys like the "UUIDs"
defined in the RFC 4122 Internet standard.  QQIDs can be identically
interconverted with UUIDs, IPv6 addresses, MD5 hashes etc., and are
suitable for a host of applications in which identifiers are read by
humans.  They are compact, can safely be transmitted in binary and text
form, can be used as components of URLs, and it can be established at a
glance whether two QQIDs are different or potentially identical.  The qqid
package contains functions to retrieve true, quantum-random QQIDs, to
generate pseudo- random QQIDs, to validate them, and to interconvert them
with other 128-bit number representations.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
