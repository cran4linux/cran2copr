%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ducklake
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with 'DuckLake' from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 2.5.0
BuildRequires:    R-CRAN-duckdb >= 1.5.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr >= 2.5.0
Requires:         R-CRAN-duckdb >= 1.5.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 

%description
A 'tidyverse'-friendly interface to 'DuckLake' <https://ducklake.select/>,
the 'DuckDB' lakehouse format. Attach versioned data lakes from R and work
with them using familiar 'dplyr' verbs, with support for ACID
transactions, time travel queries, snapshot audit trails, data inlining,
encrypted storage, multiple catalog backends ('DuckDB', 'PostgreSQL',
'SQLite', 'MySQL'), and remote access over the 'Quack' protocol from
'DuckDB'.

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
