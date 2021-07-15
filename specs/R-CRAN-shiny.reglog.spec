%global __brp_check_rpaths %{nil}
%global packname  shiny.reglog
%global packver   0.2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Optional Login and Registration Module System for ShinyApps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-scrypt 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-googlesheets4 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-scrypt 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-googlesheets4 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-lubridate 

%description
Package creates UI modules for Login, Register and Password Reset boxes
and server module for reading and writing user database contained within
googlesheet or sqlite file. Creates automatic e-mail messages after
registration and for resetting password procedure. Currently supports
English language (default) and Polish. The authentication system created
with shiny.reglog is designed to be optional: user don't need to be
logged-in to access your application, but when logged-in the user data can
be used to read from and write to relational databases.

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
