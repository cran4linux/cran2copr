%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polyglotSQL
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SQL Parsing, Analysis and Dialect Translation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 

%description
Parse, tokenize, validate, format, analyze and translate SQL between more
than 30 dialects ('PostgreSQL', 'MySQL', 'BigQuery', 'Snowflake',
'DuckDB', 'T-SQL', and others) using the 'polyglot-sql' Rust crate
<https://github.com/tobilg/polyglot>, a Rust port of the 'SQLGlot'
'Python' library.  All processing happens locally in the R session; no
database connection, 'Python' runtime or external service is required.
Includes column-level lineage, structural query analysis, query
optimization, 'AST' diffing and 'OpenLineage' facet generation.

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
