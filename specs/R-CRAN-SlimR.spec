%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SlimR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Machine Learning-Powered, Context-Matching Tool for Single-Cell and Spatial Transcriptomics Annotation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-tibble 

%description
Annotates single-cell and spatial-transcriptomic (ST) data using
context-matching marker datasets. It creates a unified marker list
(`Markers_list`) from multiple sources: built-in curated databases
('Cellmarker2', 'PanglaoDB', 'scIBD', 'TCellSI', 'PCTIT', 'PCTAM'), Seurat
objects with cell labels, or user-provided Excel tables. SlimR first uses
adaptive machine learning for parameter optimization, and then offers two
automated annotation approaches: 'cluster-based' and 'per-cell'.
Cluster-based annotation assigns one label per cluster, expression-based
probability calculation, and AUC validation. Per-cell annotation assigns
labels to individual cells using three scoring methods with adaptive
thresholds and ratio-based confidence filtering, plus optional UMAP
spatial smoothing, making it ideal for heterogeneous clusters and rare
cell types. The package also supports semi-automated workflows with
heatmaps, feature plots, and combined visualizations for manual
annotation. For more details, see Kabacoff (2020, ISBN:9787115420572).

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
