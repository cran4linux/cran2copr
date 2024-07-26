%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nodbi
%global packver   0.10.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.6
Release:          1%{?dist}%{?buildtag}
Summary:          'NoSQL' Database Connector

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-R.utils 

%description
Simplified JSON document database access and manipulation, providing a
common API across supported 'NoSQL' databases 'Elasticsearch', 'CouchDB',
'MongoDB' as well as 'SQLite/JSON1', 'PostgreSQL', and 'DuckDB'.

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
