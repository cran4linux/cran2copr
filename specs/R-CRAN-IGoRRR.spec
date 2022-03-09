%global __brp_check_rpaths %{nil}
%global packname  IGoRRR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Shiny Interface for Simple Data Management

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fuzzyjoin 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-feather 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-CRAN-tables 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-mapsf 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fuzzyjoin 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-feather 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-skimr 
Requires:         R-CRAN-tables 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-mapsf 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-magrittr 

%description
Launches a shiny application generating code to view tables in several
ways, import/export tables, modify tables, make some basic graphics.
'IGoR' is a graphic user interface designed to help beginners using simple
functions around table management and exploration. Inspired by 'Rcmdr',
'IGoR' is a code generator that, with simple inputs under a Shiny
application, provides R code mainly built around the 'tidyverse' or some
packages in the direct line of the Mosaic project: the 'rio' and
'ggformula' packages. The generated code doesn't depend on IGoR and can be
manually modified by the user or copied elsewhere.

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
