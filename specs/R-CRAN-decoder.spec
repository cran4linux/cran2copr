%global packname  decoder
%global packver   1.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.13
Release:          1%{?dist}
Summary:          Decode Coded Variables to Plain Text and the Other Way Around

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-backports 
Requires:         R-CRAN-backports 

%description
Main function "decode" is used to decode coded key values to plain text.
Function "code" can be used to code plain text to code if there is a 1:1
relation between the two. The concept relies on 'keyvalue' objects used
for translation. There are several 'keyvalue' objects included in the
areas of geographical regional codes, administrative health care unit
codes, diagnosis codes and more. It is also easy to extend the use by
arbitrary code sets.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
