%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.modules.general
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Modules for 'teal' Applications

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.60
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-sparkline >= 2.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.9
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-htmlwidgets >= 1.6.4
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-colourpicker >= 1.3.0
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-goftest >= 1.2.3
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-teal >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-tern >= 0.9.7
BuildRequires:    R-CRAN-ggrepel >= 0.9.6
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-bslib >= 0.8.0
BuildRequires:    R-CRAN-teal.data >= 0.8.0
BuildRequires:    R-CRAN-teal.transform >= 0.7.0
BuildRequires:    R-CRAN-teal.code >= 0.7.0
BuildRequires:    R-CRAN-rtables >= 0.6.11
BuildRequires:    R-CRAN-ggpp >= 0.5.8.1
BuildRequires:    R-CRAN-ggpmisc >= 0.5.6
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-teal.reporter >= 0.5.0
BuildRequires:    R-CRAN-teal.widgets >= 0.5.0
BuildRequires:    R-CRAN-teal.logger >= 0.4.0
BuildRequires:    R-CRAN-ggmosaic >= 0.3.0
BuildRequires:    R-CRAN-shinyTree >= 0.2.8
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-lattice >= 0.18.4
BuildRequires:    R-CRAN-DT >= 0.13
BuildRequires:    R-CRAN-ggExtra >= 0.10.1
BuildRequires:    R-CRAN-generics >= 0.1.3
BuildRequires:    R-CRAN-shinyvalidate >= 0.1.3
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.60
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-sparkline >= 2.0
Requires:         R-CRAN-jsonlite >= 1.8.9
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-htmlwidgets >= 1.6.4
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-colourpicker >= 1.3.0
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-goftest >= 1.2.3
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-teal >= 1.0.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-tern >= 0.9.7
Requires:         R-CRAN-ggrepel >= 0.9.6
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-bslib >= 0.8.0
Requires:         R-CRAN-teal.data >= 0.8.0
Requires:         R-CRAN-teal.transform >= 0.7.0
Requires:         R-CRAN-teal.code >= 0.7.0
Requires:         R-CRAN-rtables >= 0.6.11
Requires:         R-CRAN-ggpp >= 0.5.8.1
Requires:         R-CRAN-ggpmisc >= 0.5.6
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-teal.reporter >= 0.5.0
Requires:         R-CRAN-teal.widgets >= 0.5.0
Requires:         R-CRAN-teal.logger >= 0.4.0
Requires:         R-CRAN-ggmosaic >= 0.3.0
Requires:         R-CRAN-shinyTree >= 0.2.8
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-lattice >= 0.18.4
Requires:         R-CRAN-DT >= 0.13
Requires:         R-CRAN-ggExtra >= 0.10.1
Requires:         R-CRAN-generics >= 0.1.3
Requires:         R-CRAN-shinyvalidate >= 0.1.3
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Prebuilt 'shiny' modules containing tools for viewing data, visualizing
data, understanding missing and outlier values within your data and
performing simple data analysis.  This extends 'teal' framework that
supports reproducible research and analysis.

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
