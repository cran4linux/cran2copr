%global packname  rorcid
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          3%{?dist}
Summary:          Interface to the 'Orcid.org' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-fauxpas >= 0.2.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-fauxpas >= 0.2.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-data.table 

%description
Client for the 'Orcid.org' API (<https://orcid.org/>). Functions included
for searching for people, searching by 'DOI', and searching by 'Orcid'
'ID'.

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
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
