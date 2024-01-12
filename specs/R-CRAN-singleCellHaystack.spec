%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  singleCellHaystack
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Universal Differential Expression Prediction Tool for Single-Cell and Spatial Genomics Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
One key exploratory analysis step in single-cell genomics data analysis is
the prediction of features with different activity levels. For example, we
want to predict differentially expressed genes (DEGs) in single-cell
RNA-seq data, spatial DEGs in spatial transcriptomics data, or
differentially accessible regions (DARs) in single-cell ATAC-seq data.
'singleCellHaystack' predicts differentially active features in single
cell omics datasets without relying on the clustering of cells into
arbitrary clusters. 'singleCellHaystack' uses Kullback-Leibler divergence
to find features (e.g., genes, genomic regions, etc) that are active in
subsets of cells that are non-randomly positioned inside an input space
(such as 1D trajectories, 2D tissue sections, multi-dimensional
embeddings, etc). For the theoretical background of 'singleCellHaystack'
we refer to our original paper Vandenbon and Diez (Nature Communications,
2020) <doi:10.1038/s41467-020-17900-3> and our update Vandenbon and Diez
(Scientific Reports, 2023) <doi:10.1038/s41598-023-38965-2>.

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
