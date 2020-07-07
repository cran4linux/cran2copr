%global packname  atsd
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Support Querying Axibase Time-Series Database

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl >= 1.95.4.5
BuildRequires:    R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-RCurl >= 1.95.4.5
Requires:         R-CRAN-httr >= 0.6.1

%description
Provides functions for retrieving time-series and related meta-data such
as entities, metrics, and tags from the Axibase Time-Series Database
(ATSD). ATSD is a non-relational clustered database used for storing
performance measurements from IT infrastructure resources: servers,
network devices, storage systems, and applications.

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
%doc %{rlibdir}/%{packname}/connection.config
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NOTICE
%{rlibdir}/%{packname}/INDEX
