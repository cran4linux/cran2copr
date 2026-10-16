%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RTrino
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'DBI' Backend for 'Trino'

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI >= 1.2.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI >= 1.2.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
A 'DBI' compliant backend for 'Trino' <https://trino.io>, the distributed
SQL query engine (successor of 'PrestoSQL'). Connects to a 'Trino' cluster
over its HTTP REST API, executes queries with automatic pagination, maps
'Trino' types to R types, and integrates with 'dplyr' through 'dbplyr' SQL
dialects. Supports basic, JSON Web Token (JWT) bearer and OAuth2 client
credentials authentication, as well as custom certificate authorities.

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
