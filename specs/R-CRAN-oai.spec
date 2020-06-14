%global debug_package %{nil}
%global packname  oai
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          General Purpose 'Oai-PMH' Services Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-httr >= 1.2.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-httr >= 1.2.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-xml2 >= 1.0.0

%description
A general purpose client to work with any 'OAI-PMH' (Open Archives
Initiative Protocol for 'Metadata' Harvesting) service. The 'OAI-PMH'
protocol is described at
<http://www.openarchives.org/OAI/openarchivesprotocol.html>. Functions are
provided to work with the 'OAI-PMH' verbs: 'GetRecord', 'Identify',
'ListIdentifiers', 'ListMetadataFormats', 'ListRecords', and 'ListSets'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
