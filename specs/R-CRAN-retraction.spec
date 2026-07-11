%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  retraction
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detect Retracted References in Documents and Bibliographies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Scans manuscripts, bibliographies, and reference lists for citations to
retracted publications so that authors can avoid citing retracted work.
'retraction' reads bibliographic formats (BibTeX, BibLaTeX, CSL-JSON, RIS,
EndNote XML) and document formats (R Markdown, Quarto, 'LaTeX', Markdown,
HTML, JATS XML, Word, and PDF), extracts and normalizes identifiers, and
checks them against retraction data. The default data source is the
Retraction Watch database served through the 'XeraRetractionTracker' API;
'Crossref', 'OpenAlex', 'Europe PMC', 'PubMed', 'DataCite', and a preprint
source ('arXiv' and 'bioRxiv' withdrawals) are available as additional
sources ('OpenAlex' retraction data is itself derived from Retraction
Watch). Within each source, matching proceeds from exact Digital Object
Identifier (DOI) and 'PubMed' identifier lookups to fuzzy title matching,
and results are returned as a tidy table with a match-quality score and an
optional self-contained HTML report.

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
