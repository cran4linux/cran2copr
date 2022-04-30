%global __brp_check_rpaths %{nil}
%global packname  stacomirtools
%global packver   0.6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connection Class for Package stacomiR

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RPostgres 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-pool 
Requires:         R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-utils 
Requires:         R-CRAN-RPostgres 

%description
S4 class wrappers for the 'ODBC' and Pool DBI connection, also provides
some utilities to paste small datasets to clipboard, rename columns. It is
used by the package 'stacomiR' for connections to the database.
Development versions of 'stacomiR' are available in R-forge.

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
