%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RPostgreSQL
%global packver   0.7-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to the 'PostgreSQL' Database System

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libpq-devel
BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-DBI >= 0.3
BuildRequires:    R-methods 
Requires:         R-CRAN-DBI >= 0.3
Requires:         R-methods 

%description
Database interface and 'PostgreSQL' driver for 'R'. This package provides
a Database Interface 'DBI' compliant driver for 'R' to access 'PostgreSQL'
database systems. In order to build and install this package from source,
'PostgreSQL' itself must be present your system to provide 'PostgreSQL'
functionality via its libraries and header files. These files are provided
as 'postgresql-devel' package under some Linux distributions. On 'macOS'
and 'Microsoft Windows' system the attached 'libpq' library source will be
used.

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
