%global packname  deeplr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Interface to the 'DeepL' Translation API

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-utf8 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-utf8 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-stringr 

%description
A wrapper for the 'DeepL' API, a web service for translating texts between
different languages. Access to the official API (see
<https://www.deepl.com/translator>) is subject to a monthly fee. No
authentication key is required for the undocumented DeepL JSON-RPC API.
The package provides functions for both types of API calls.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
