%global packname  emld
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          Ecological Metadata as Linked Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonld 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonld 
Requires:         R-methods 
Requires:         R-CRAN-yaml 

%description
This is a utility for transforming Ecological Metadata Language ('EML')
files into 'JSON-LD' and back into 'EML.'  Doing so creates a list-based
representation of 'EML' in R, so that 'EML' data can easily be manipulated
using standard 'R' tools. This makes this package an effective backend for
other 'R'-based tools working with 'EML.' By abstracting away the
complexity of 'XML' Schema, developers can build around native 'R' list
objects and not have to worry about satisfying many of the additional
constraints of set by the schema (such as element ordering, which is
handled automatically). Additionally, the 'JSON-LD' representation enables
the use of developer-friendly 'JSON' parsing and serialization that may
facilitate the use of 'EML' in contexts outside of 'R,' as well as the
informatics-friendly serializations such as 'RDF' and 'SPARQL' queries.

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
