%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Seurat
%global packver   4.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Single Cell Genomics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-plotly >= 4.9.0
BuildRequires:    R-CRAN-SeuratObject >= 4.1.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-scattermore >= 1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-sctransform >= 0.4.0
BuildRequires:    R-CRAN-leiden >= 0.3.1
BuildRequires:    R-CRAN-uwot >= 0.1.14
BuildRequires:    R-CRAN-RcppAnnoy >= 0.0.18
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-plotly >= 4.9.0
Requires:         R-CRAN-SeuratObject >= 4.1.4
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-scattermore >= 1.2
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-sctransform >= 0.4.0
Requires:         R-CRAN-leiden >= 0.3.1
Requires:         R-CRAN-uwot >= 0.1.14
Requires:         R-CRAN-RcppAnnoy >= 0.0.18
Requires:         R-methods 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggridges 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-png 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
A toolkit for quality control, analysis, and exploration of single cell
RNA sequencing data. 'Seurat' aims to enable users to identify and
interpret sources of heterogeneity from single cell transcriptomic
measurements, and to integrate diverse types of single cell data. See
Satija R, Farrell J, Gennert D, et al (2015) <doi:10.1038/nbt.3192>,
Macosko E, Basu A, Satija R, et al (2015)
<doi:10.1016/j.cell.2015.05.002>, Stuart T, Butler A, et al (2019)
<doi:10.1016/j.cell.2019.05.031>, and Hao, Hao, et al (2020)
<doi:10.1101/2020.10.12.335331> for more details.

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
