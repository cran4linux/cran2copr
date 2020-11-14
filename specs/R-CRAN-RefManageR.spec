%global packname  RefManageR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Straightforward 'BibTeX' and 'BibLaTeX' Bibliography Management

License:          GPL-2 | GPL-3 | BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.5.0
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
Requires:         R-CRAN-lubridate >= 1.5.0
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-tools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-methods 

%description
Provides tools for importing and working with bibliographic references. It
greatly enhances the 'bibentry' class by providing a class 'BibEntry'
which stores 'BibTeX' and 'BibLaTeX' references, supports 'UTF-8'
encoding, and can be easily searched by any field, by date ranges, and by
various formats for name lists (author by last names, translator by full
names, etc.). Entries can be updated, combined, sorted, printed in a
number of styles, and exported. 'BibTeX' and 'BibLaTeX' '.bib' files can
be read into 'R' and converted to 'BibEntry' objects. Interfaces to 'NCBI
Entrez', 'CrossRef', and 'Zotero' are provided for importing references
and references can be created from locally stored 'PDF' files using
'Poppler'. Includes functions for citing and generating a bibliography
with hyperlinks for documents prepared with 'RMarkdown' or 'RHTML'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
