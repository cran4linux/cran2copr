%global packname  medrxivr
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Search MedRxiv and BioRxiv Preprint Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-bib2df 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-bib2df 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-lubridate 

%description
An increasingly important source of health-related bibliographic content
are preprints - preliminary versions of research articles that have yet to
undergo peer review. The two preprint repositories most relevant to
health-related sciences are medRxiv <https://www.medrxiv.org/> and bioRxiv
<https://www.biorxiv.org/>, both of which are operated by the Cold Spring
Harbor Laboratory. 'medrxivr' provides programmatic access to the 'Cold
Spring Harbour Laboratory (CSHL)' API <https://api.biorxiv.org/>, allowing
users to easily download medRxiv and bioRxiv preprint metadata (e.g.
title, abstract, publication date, author list, etc) into R. 'medrxivr'
also provides functions to search the downloaded preprint records using
regular expressions and Boolean logic, as well as helper functions that
allow users to export their search results to a .BIB file for easy import
to a reference manager and to download the full-text PDFs of preprints
matching their search criteria.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
