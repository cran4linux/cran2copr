%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VizModules
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible, Interactive 'shiny' Modules for Almost Any Plot

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-plotthis >= 0.11.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dittoViz 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-roclang 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-plotthis >= 0.11.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dittoViz 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-roclang 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-htmlwidgets 

%description
Offers a core selection of interactivity-first 'shiny' modules for many
plot types meant to serve as flexible building blocks for applications and
as the base for more complex modules. These modules allow for the rapid
and convenient construction of 'shiny' apps with very few lines of code
and decouple plotting from the underlying data. These modules allow for
full plot aesthetic customization by the end user through UI inputs.
Utility functions for simple UI organization, automated UI tooltips, and
additional plot enhancements are also provided.

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
