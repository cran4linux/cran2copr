%global packname  rdryad
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Access for Dryad Web Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-solrium >= 1.0.0
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-CRAN-oai >= 0.2.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-curl >= 3.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-solrium >= 1.0.0
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-CRAN-oai >= 0.2.2
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 

%description
Interface to the Dryad "Solr" API, their "OAI-PMH" service, and fetch
datasets. Dryad (<http://datadryad.org/>) is a curated host of data
underlying scientific publications.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/mets.xsd
%{rlibdir}/%{packname}/INDEX
