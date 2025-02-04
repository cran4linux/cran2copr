%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  writer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Write from Multiple Sources to a Database Table

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-dbplyr >= 2.3.1
BuildRequires:    R-CRAN-glue >= 1.5.1
BuildRequires:    R-CRAN-DBI >= 1.2.3
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-dbplyr >= 2.3.1
Requires:         R-CRAN-glue >= 1.5.1
Requires:         R-CRAN-DBI >= 1.2.3
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.0

%description
Provides unified syntax to write data from lazy 'dplyr' 'tbl' or 'dplyr'
'sql' query or a dataframe to a database table with modes such as create,
append, insert, update, upsert, patch, delete, overwrite,
overwrite_schema.

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
