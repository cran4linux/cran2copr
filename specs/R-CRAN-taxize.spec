%global packname  taxize
%global packver   0.9.93
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.93
Release:          1%{?dist}
Summary:          Taxonomic Information from Around the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rotl >= 3.0.0
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-bold >= 0.8.6
BuildRequires:    R-CRAN-ritis >= 0.7.6
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-rredlist >= 0.5.0
BuildRequires:    R-CRAN-worrms >= 0.4.0
BuildRequires:    R-CRAN-natserv >= 0.3.0
BuildRequires:    R-CRAN-wikitaxa >= 0.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-phangorn 
Requires:         R-CRAN-rotl >= 3.0.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-bold >= 0.8.6
Requires:         R-CRAN-ritis >= 0.7.6
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-rredlist >= 0.5.0
Requires:         R-CRAN-worrms >= 0.4.0
Requires:         R-CRAN-natserv >= 0.3.0
Requires:         R-CRAN-wikitaxa >= 0.3.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-phangorn 

%description
Interacts with a suite of web 'APIs' for taxonomic tasks, such as getting
database specific taxonomic identifiers, verifying species names, getting
taxonomic hierarchies, fetching downstream and upstream taxonomic names,
getting taxonomic synonyms, converting scientific to common names and vice
versa, and more.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/ignore
%{rlibdir}/%{packname}/INDEX
