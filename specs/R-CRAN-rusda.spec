%global packname  rusda
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to USDA Databases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 0.6.1
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-RCurl 

%description
An interface to the web service methods provided by the United States
Department of Agriculture (USDA). The Agricultural Research Service (ARS)
provides a large set of databases. The current version of the package
holds interfaces to the Systematic Mycology and Microbiology Laboratory
(SMML), which consists of four databases: Fungus-Host Distributions,
Specimens, Literature and the Nomenclature database. It provides functions
for querying these databases. The main function is code{associations},
which allows searching for fungus-host combinations.

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
%{rlibdir}/%{packname}/INDEX
