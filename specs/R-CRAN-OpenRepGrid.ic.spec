%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OpenRepGrid.ic
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretive Clustering for Repertory Grids

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tidyverse 
Requires:         R-CRAN-shinydashboardPlus >= 2.0.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-splines 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tidyverse 

%description
Shiny UI to identify cliques of related constructs in repertory grid data.
See Burr, King, & Heckmann (2020) <doi:10.1080/14780887.2020.1794088> for
a description of the interpretive clustering (IC) method.

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
