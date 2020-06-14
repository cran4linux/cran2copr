%global packname  tm.plugin.webmining
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Retrieve Structured, Textual Data from Various Web Sources

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-NLP >= 0.1.2
BuildRequires:    R-CRAN-boilerpipeR 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-RJSONIO 
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-NLP >= 0.1.2
Requires:         R-CRAN-boilerpipeR 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-RJSONIO 

%description
Facilitate text retrieval from feed formats like XML (RSS, ATOM) and JSON.
Also direct retrieval from HTML is supported. As most (news) feeds only
incorporate small fractions of the original text tm.plugin.webmining even
retrieves and extracts the text of the original text source.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
