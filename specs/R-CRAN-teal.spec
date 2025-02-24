%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Web Apps for Analyzing Clinical Trials Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-teal.data >= 0.7.0
BuildRequires:    R-CRAN-teal.code >= 0.6.1
BuildRequires:    R-CRAN-teal.slice >= 0.6.0
BuildRequires:    R-CRAN-teal.widgets >= 0.4.3
BuildRequires:    R-CRAN-teal.reporter >= 0.4.0
BuildRequires:    R-CRAN-teal.logger >= 0.3.2
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-logger >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-teal.data >= 0.7.0
Requires:         R-CRAN-teal.code >= 0.6.1
Requires:         R-CRAN-teal.slice >= 0.6.0
Requires:         R-CRAN-teal.widgets >= 0.4.3
Requires:         R-CRAN-teal.reporter >= 0.4.0
Requires:         R-CRAN-teal.logger >= 0.3.2
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-logger >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A 'shiny' based interactive exploration framework for analyzing clinical
trials data. 'teal' currently provides a dynamic filtering facility and
different data viewers. 'teal' 'shiny' applications are built using
standard 'shiny' modules.

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
