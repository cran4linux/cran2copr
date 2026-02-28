%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpaCCI
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Aware Cell-Cell Interaction Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Seurat >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-circlize >= 0.4.12
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Seurat >= 4.0.0
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-circlize >= 0.4.12
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-patchwork 
Requires:         R-grDevices 
Requires:         R-CRAN-reshape2 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-rlang 

%description
Provides tools for analyzing spatial cell-cell interactions based on
ligand-receptor pairs, including functions for local, regional, and global
analysis using spatial transcriptomics data. Integrates with databases
like 'CellChat' <https://github.com/jinworks/CellChat>, 'CellPhoneDB'
<https://www.cellphonedb.org/>, 'Cellinker'
<https://www.rna-society.org/cellinker/>, 'ICELLNET'
<https://github.com/soumelis-lab/ICELLNET>, and 'ConnectomeDB'
<https://humanconnectome.org/software/connectomedb/> to identify
ligand-receptor pairs, visualize interactions through heatmaps, chord
diagrams, and infer interactions on different spatial scales.

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
