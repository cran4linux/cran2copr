%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSQLite.toolkit
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Load Data in SQLite from Tabular Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.3.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-openxlsx2 
BuildRequires:    R-CRAN-arrow 
Requires:         R-CRAN-RSQLite >= 2.3.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-openxlsx2 
Requires:         R-CRAN-arrow 

%description
A lightweight wrapper around the 'RSQLite' package for streamlined loading
of data from tabular files (i,e. text delimited files like Comma Separated
Values and Tab Separated Values, Microsoft Excel, and Arrow Inter-process
Communication files) in 'SQLite' databases. Includes helper functions for
inspecting the structure of the input files, and some functions to
simplify activities on the 'SQLite' tables.

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
