%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inDAGO
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A GUI for Dual and Bulk RNA-Sequencing Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bigtabulate 
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-heatmaply 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-memuse 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-spsComps 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-upsetjs 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-utils 
Requires:         R-CRAN-bigtabulate 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-CRAN-heatmaply 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-memuse 
Requires:         R-methods 
Requires:         R-CRAN-paletteer 
Requires:         R-parallel 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-spsComps 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-upsetjs 
Requires:         R-CRAN-UpSetR 
Requires:         R-utils 

%description
A 'shiny' app that supports both dual and bulk RNA-seq, with the dual
RNA-seq functionality offering the flexibility to perform either a
sequential approach (where reads are mapped separately to each genome) or
a combined approach (where reads are aligned to a single merged genome).
The user-friendly interface automates the analysis process, providing
step-by-step guidance, making it easy for users to navigate between
different analysis steps, and download intermediate results and
publication-ready plots.

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
