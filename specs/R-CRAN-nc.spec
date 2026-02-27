%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nc
%global packver   2026.2.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2026.2.20
Release:          1%{?dist}%{?buildtag}
Summary:          Named Capture to Data Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-data.table >= 1.15.0

%description
User-friendly functions for extracting a data table (row for each match,
column for each group) from non-tabular text data using regular
expressions, and for melting columns that match a regular expression.
Patterns are defined using a readable syntax that makes it easy to build
complex patterns in terms of simpler, re-usable sub-patterns. Named R
arguments are translated to column names in the output; capture groups
without names are used internally in order to provide a standard interface
to three regular expression 'C' libraries ('PCRE', 'RE2', 'ICU'). Output
can also include numeric columns via user-specified type conversion
functions.

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
