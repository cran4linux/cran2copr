%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdflib
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Manipulate and Query Semantic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-redland 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-redland 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
The Resource Description Framework, or 'RDF' is a widely used data
representation model that forms the cornerstone of the Semantic Web. 'RDF'
represents data as a graph rather than the familiar data table or
rectangle of relational databases. The 'rdflib' package provides a
friendly and concise user interface for performing common tasks on 'RDF'
data, such as reading, writing and converting between the various
serializations of 'RDF' data, including 'rdfxml', 'turtle', 'nquads',
'ntriples', and 'json-ld'; creating new 'RDF' graphs, and performing graph
queries using 'SPARQL'. This package wraps the low level 'redland' R
package which provides direct bindings to the 'redland' C library.
Additionally, the package supports the newer and more developer friendly
'JSON-LD' format through the 'jsonld' package. The package interface takes
inspiration from the Python 'rdflib' library.

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
