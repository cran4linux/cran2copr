%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  abstractExtractR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve and Audit Scholarly Metadata from Multiple Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 

%description
Retrieves and normalizes scholarly article metadata and abstracts from the
'Crossref' REST API
<https://www.crossref.org/documentation/retrieve-metadata/rest-api/>, the
'OpenAlex' API <https://help.openalex.org/> and the 'Scopus' Search API
<https://dev.elsevier.com/sc_apis.html>. Provides bibliographic searches,
cursor pagination, publication date and author filtering, abstract
retrieval by Digital Object Identifier (DOI), cached batch enrichment,
merging of duplicate records, metadata-quality audits, reproducible search
snapshots, local archives with integrity verification, and export to
comma-separated values (CSV), 'BibTeX' and 'RIS' citation files. Network
requests support configurable timeouts and test callbacks. 'Scopus'
searches require an 'Elsevier' API key; 'Crossref' queries do not.
'OpenAlex' supports limited keyless searches and authenticated pagination.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
