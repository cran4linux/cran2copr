%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyNotes
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny Module for Taking Free-Form Notes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
An enterprise-targeted scalable and customizable 'shiny' module providing
an easy way to incorporate free-form note taking or discussion boards into
applications. The package includes a 'shiny' module that can be included
in any 'shiny' application to create a panel containing searchable,
editable text broken down by section headers. Can be used with a local
'SQLite' database, or a compatible remote database of choice.

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
