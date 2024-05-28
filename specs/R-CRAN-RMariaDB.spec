%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMariaDB
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Database Interface and MariaDB Driver

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mariadb-devel
BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildRequires:    R-CRAN-DBI >= 1.1.3
BuildRequires:    R-CRAN-hms >= 0.5.0
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-blob 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cpp11 
BuildRequires:    R-CRAN-plogr 
Requires:         R-CRAN-DBI >= 1.1.3
Requires:         R-CRAN-hms >= 0.5.0
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-blob 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Implements a DBI-compliant interface to MariaDB (<https://mariadb.org/>)
and MySQL (<https://www.mysql.com/>) databases.

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
