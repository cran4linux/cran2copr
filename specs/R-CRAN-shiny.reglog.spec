%global __brp_check_rpaths %{nil}
%global packname  shiny.reglog
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optional Login and Registration Module System for ShinyApps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-scrypt 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-scrypt 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-uuid 

%description
RegLog system provides a set of shiny modules to handle register procedure
for your users, alongside with login, edit credentials and password reset
functionality. It provides support for popular SQL databases and
optionally googlesheet-based database for easy setup. For email sending it
provides support for 'emayili' and 'gmailr' backends. Architecture makes
customizing usability pretty straightforward. The authentication system
created with shiny.reglog is designed to be optional: user don't need to
be logged-in to access your application, but when logged-in the user data
can be used to read from and write to relational databases.

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
