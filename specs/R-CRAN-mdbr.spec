%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mdbr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Work with Microsoft Access Files

License:          GPL-3 | LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       mdbtools
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 

%description
Work with Microsoft Access '.mdb' and '.accdb' files using the open source
'MDB Tools' library <https://github.com/mdbtools/mdbtools/>. The library
is compiled and bundled with the package, so no external installation is
required. Provides high-level helpers for reading tables, exporting to CSV
or JSON, inspecting table definitions, and running SQL queries. Also
exposes a full read-only 'DBI' interface for use with standard database
workflows.

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
