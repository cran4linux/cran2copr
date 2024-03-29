%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viewpoly
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Shiny App to Visualize Genetic Maps and QTL Analysis in Polyploid Species

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-golem >= 0.3.1
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-JBrowseR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-hidecan 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-golem >= 0.3.1
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-JBrowseR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-markdown 
Requires:         R-stats 
Requires:         R-CRAN-hidecan 
Requires:         R-CRAN-purrr 

%description
Provides a graphical user interface to integrate, visualize and explore
results from linkage and quantitative trait loci analysis, together with
genomic information for autopolyploid species. The app is meant for
interactive use and allows users to optionally upload different sources of
information, including gene annotation and alignment files, enabling the
exploitation and search for candidate genes in a genome browser. In its
current version, 'VIEWpoly' supports inputs from 'MAPpoly', 'polymapR',
'diaQTL', 'QTLpoly', 'polyqtlR', 'GWASpoly', and 'HIDECAN' packages.

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
