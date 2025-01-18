%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyscholar
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Template for Creating Reproducible 'shiny' Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-gargoyle 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-gargoyle 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-tools 
Requires:         R-CRAN-zip 

%description
Create a skeleton 'shiny' application with create_template() that is
reproducible, can be saved and meets academic standards for attribution.
Forked from 'wallace'. Code is split into modules that are loaded and
linked together automatically and each call one function. Guidance pages
explain modules to users and flexible logging informs them of any errors.
Options enable asynchronous operations, viewing of source code,
interactive maps and data tables. Use to create complex analytical
applications, following best practices in open science and software
development. Includes functions for automating repetitive development
tasks and an example application at run_shinyscholar() that requires
install.packages("shinyscholar", dependencies = TRUE). A guide to
developing applications can be found on the package website.

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
