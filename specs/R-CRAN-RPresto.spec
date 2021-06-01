%global packname  RPresto
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          DBI Connector to Presto

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-httr >= 0.6
BuildRequires:    R-CRAN-DBI >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr >= 0.6
Requires:         R-CRAN-DBI >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringi 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a 'DBI' compliant interface to Presto. Presto is an open source
distributed SQL query engine for running interactive analytic queries
against data sources of all sizes ranging from gigabytes to petabytes:
<https://prestodb.io/>.

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
