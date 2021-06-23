%global __brp_check_rpaths %{nil}
%global packname  ShinyQuickStarter
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'RStudio' Addin for Building Shiny Apps per Drag & Drop

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-shinyjs >= 2.0
BuildRequires:    R-CRAN-shinyalert >= 2.0
BuildRequires:    R-CRAN-shiny >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-stringi >= 1.4
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-styler >= 1.3
BuildRequires:    R-CRAN-data.table >= 1.13
BuildRequires:    R-CRAN-colourpicker >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-shinyFiles >= 0.9
BuildRequires:    R-CRAN-shinydashboard >= 0.7
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-plotly >= 4.9
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-shinyjs >= 2.0
Requires:         R-CRAN-shinyalert >= 2.0
Requires:         R-CRAN-shiny >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-stringi >= 1.4
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-styler >= 1.3
Requires:         R-CRAN-data.table >= 1.13
Requires:         R-CRAN-colourpicker >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-shinyFiles >= 0.9
Requires:         R-CRAN-shinydashboard >= 0.7
Requires:         R-CRAN-shinyWidgets >= 0.5.7
Requires:         R-stats 
Requires:         R-CRAN-fs 

%description
This 'RStudio' addin makes the creation of 'Shiny' and 'ShinyDashboard'
apps more efficient.  Besides the necessary folder structure, entire apps
can be created using a drag and drop interface and customized with respect
to a specific use case. The addin allows the export of the required user
interface and server code at any time. By allowing the creation of
modules, the addin can be used throughout the entire app development
process.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
