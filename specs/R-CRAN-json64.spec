%global packname  json64
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          A 'Base64' Encode/Decode Package with Support for JSONOutput/Input and UTF-8

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-jsonlite 

%description
Encode/Decode 'base64', with support for JSON format, using two functions:
j_encode() and j_decode().  'Base64' is a group of similar binary-to-text
encoding schemes that represent binary data in an ASCII string format by
translating it into a radix-64 representation, used when there is a need
to encode binary data that needs to be stored and transferred over media
that are designed to deal with textual data, ensuring that the data will
remain intact and without modification during transport.
<https://developer.mozilla.org/en-US/docs/Web/API/WindowBase64/Base64_encoding_and_decoding>
On the other side, JSON (JavaScript Object Notation) is a lightweight
data-interchange format. Easy to read, write, parse and generate. It is
based on a subset of the JavaScript Programming Language. JSON is a text
format that is completely language independent but uses conventions that
are familiar to programmers of the C-family of languages, including C,
C++, C#, Java, JavaScript, Perl, Python, and many others. JSON structure
is built around name:value pairs and ordered list of values.
<https://www.json.org> The first function, j_encode(), let you transform a
data.frame or list to a 'base64' encoded JSON (or JSON string).  The
j_decode() function takes a 'base64' string (could be an encoded JSON) and
transform it to a data.frame (or list, depending of the JSON structure).

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
%{rlibdir}/%{packname}/INDEX
