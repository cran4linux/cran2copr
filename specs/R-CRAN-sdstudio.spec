%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdstudio
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Companion Application for the 'surveydown' Survey Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dotenv 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-surveydown 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dotenv 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-later 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-surveydown 

%description
Companion package that supports the 'surveydown' survey platform
(<https://surveydown.org>). The default method for working with a
'surveydown' survey is to edit the plain text 'survey.qmd' and 'app.R'
files. With 'sdstudio', you can create, preview and manage surveys with a
'shiny' application as a graphical user interface.

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
