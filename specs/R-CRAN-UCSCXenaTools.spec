%global packname  UCSCXenaTools
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          Download and Explore Datasets from UCSC Xena Data Hubs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readr 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 

%description
Download and explore datasets from UCSC Xena data hubs, which are a
collection of UCSC-hosted public databases such as TCGA, ICGC, TARGET,
GTEx, CCLE, and others. Databases are normalized so they can be combined,
linked, filtered, explored and downloaded.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/api.RData
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/dataset_metadata.RData
%doc %{rlibdir}/%{packname}/develop.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/queries
%doc %{rlibdir}/%{packname}/test_api.R
%{rlibdir}/%{packname}/INDEX
