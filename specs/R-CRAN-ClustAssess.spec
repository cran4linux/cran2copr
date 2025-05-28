%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClustAssess
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Assessing Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-Gmedian 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrastr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-gprofiler2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leiden 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-qualpalr 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyLP 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-vioplot 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-Gmedian 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrastr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-gprofiler2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leiden 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-qualpalr 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyLP 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-utils 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-vioplot 

%description
A set of tools for evaluating clustering robustness using proportion of
ambiguously clustered pairs (Senbabaoglu et al. (2014)
<doi:10.1038/srep06207>), as well as similarity across methods and method
stability using element-centric clustering comparison (Gates et al. (2019)
<doi:10.1038/s41598-019-44892-y>). Additionally, this package enables
stability-based parameter assessment for graph-based clustering pipelines
typical in single-cell data analysis.

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
