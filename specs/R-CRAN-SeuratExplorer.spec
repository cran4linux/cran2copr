%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SeuratExplorer
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          An 'Shiny' App for Exploring scRNA-seq Data Processed in 'Seurat'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 5.4.0
BuildRequires:    R-CRAN-SeuratObject >= 5.3.0
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-patchwork >= 1.3.2
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-markdown 
Requires:         R-CRAN-Seurat >= 5.4.0
Requires:         R-CRAN-SeuratObject >= 5.3.0
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-patchwork >= 1.3.2
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-markdown 

%description
A simple, one-command package which runs an interactive dashboard capable
of common visualizations for single cell RNA-seq. 'SeuratExplorer'
requires a processed 'Seurat' object, which is saved as 'rds' or 'qs2'
file.

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
