%global __brp_check_rpaths %{nil}
%global packname  virtuoso
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Virtuoso' using 'ODBC'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-odbc 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ini 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ps 
Requires:         R-CRAN-odbc 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-DBI 
Requires:         R-utils 
Requires:         R-CRAN-ini 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ps 

%description
Provides users with a simple and convenient mechanism to manage and query
a 'Virtuoso' database using the 'DBI' (Data-Base Interface) compatible
'ODBC' (Open Database Connectivity) interface. 'Virtuoso' is a
high-performance "universal server," which can act as both a relational
database, supporting standard Structured Query Language ('SQL') queries,
while also supporting data following the Resource Description Framework
('RDF') model for Linked Data. 'RDF' data can be queried using 'SPARQL'
('SPARQL' Protocol and 'RDF' Query Language) queries, a graph-based query
that supports semantic reasoning. This allows users to leverage the
performance of local or remote 'Virtuoso' servers using popular 'R'
packages such as 'DBI' and 'dplyr', while also providing a
high-performance solution for working with large 'RDF' 'triplestores' from
'R.' The package also provides helper routines to install, launch, and
manage a 'Virtuoso' server locally on 'Mac', 'Windows' and 'Linux'
platforms using the standard interactive installers from the 'R'
command-line.  By automatically handling these setup steps, the package
can make using 'Virtuoso' considerably faster and easier for a most users
to deploy in a local environment. Managing the bulk import of triples from
common serializations with a single intuitive command is another key
feature of this package.  Bulk import performance can be tens to hundreds
of times faster than the comparable imports using existing 'R' tools,
including 'rdflib' and 'redland' packages.

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
