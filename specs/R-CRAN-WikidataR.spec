%global __brp_check_rpaths %{nil}
%global packname  WikidataR
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Read-Write API Client Library for Wikidata

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-WikipediR 
BuildRequires:    R-CRAN-WikidataQueryServiceR 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-WikipediR 
Requires:         R-CRAN-WikidataQueryServiceR 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-crayon 
Requires:         R-utils 

%description
Read from, interogate, and write to Wikidata <https://www.wikidata.org> -
the multilingual, interdisciplinary, semantic knowledgebase. Includes
functions to: read from wikidata (single items, properties, or
properties); query wikidata (retrieving all items that match a set of
criterial via Wikidata SPARQL query service); write to Wikidata (adding
new items or statements via QuickStatements); and handle and manipulate
Wikidata objects (as lists and tibbles). Uses the Wikidata and
Quickstatements APIs.

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
