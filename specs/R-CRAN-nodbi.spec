%global __brp_check_rpaths %{nil}
%global packname  nodbi
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          'NoSQL' Database Connector

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.2.4
BuildRequires:    R-CRAN-mongolite >= 1.6
BuildRequires:    R-CRAN-elastic >= 1.0.0
BuildRequires:    R-CRAN-sofa >= 0.3.0
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-RSQLite >= 2.2.4
Requires:         R-CRAN-mongolite >= 1.6
Requires:         R-CRAN-elastic >= 1.0.0
Requires:         R-CRAN-sofa >= 0.3.0
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonify 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-DBI 

%description
Simplified document database access and manipulation, providing a common
API across supported 'NoSQL' databases 'Elasticsearch', 'CouchDB',
'MongoDB' as well as 'SQLite/JSON1' and 'PostgreSQL'.

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
