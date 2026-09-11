%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icebergr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write 'Apache Iceberg' Tables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-nanoarrow >= 0.4.0
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-nanoarrow >= 0.4.0
Requires:         R-CRAN-tibble 

%description
A native client for 'Apache Iceberg', the open table format used by
'Snowflake', 'Databricks', 'BigQuery', 'AWS' and 'Dremio'. R has otherwise
been able to read 'Iceberg' tables only by routing through 'DuckDB' as an
intermediary, which rules out writes, snapshot management and catalog
integration. This package talks to 'Iceberg' directly: it connects to REST
and 'AWS Glue' catalogs, lists namespaces and tables, reads the schema and
partition specification of a table, scans data with predicates and
projections pushed down, travels back through snapshot history, and
appends new data. 'Apache Arrow' is the interchange layer throughout, so
scan results arrive in R without a serialisation round trip. Built on
'iceberg-rust', the Apache-governed 'Rust' implementation, via 'extendr'.
Supports table spec versions 1 and 2; see the 'README' for the full matrix
of supported and unsupported features. This is a community package, not
affiliated with or endorsed by The Apache Software Foundation; 'Apache',
'Apache Iceberg' and 'Iceberg' are trademarks of The Apache Software
Foundation.

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
