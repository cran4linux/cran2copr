%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taxize
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-natserv >= 1.0.0
BuildRequires:    R-CRAN-ritis >= 0.7.6
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-worrms >= 0.4.0
BuildRequires:    R-CRAN-wikitaxa >= 0.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rredlist 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-rotl >= 3.0.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-natserv >= 1.0.0
Requires:         R-CRAN-ritis >= 0.7.6
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-worrms >= 0.4.0
Requires:         R-CRAN-wikitaxa >= 0.3.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rredlist 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-stringi 

%description
Interacts with a suite of web application programming interfaces (API) for
taxonomic tasks, such as getting database specific taxonomic identifiers,
verifying species names, getting taxonomic hierarchies, fetching
downstream and upstream taxonomic names, getting taxonomic synonyms,
converting scientific to common names and vice versa, and more. Some of
the services supported include 'NCBI E-utilities'
(<https://www.ncbi.nlm.nih.gov/books/NBK25501/>), 'Encyclopedia of Life'
(<https://eol.org/docs/what-is-eol/data-services>), 'Global Biodiversity
Information Facility' (<https://techdocs.gbif.org/en/openapi/>), and many
more. Links to the API documentation for other supported services are
available in the documentation for their respective functions in this
package.

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
