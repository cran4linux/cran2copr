%global packname  singleCellHaystack
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Finding Needles (=differentially Expressed Genes) in Haystacks (=single Cell Data)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Identification of differentially expressed genes (DEGs) is a key step in
single-cell transcriptomics data analysis. 'singleCellHaystack' predicts
DEGs without relying on clustering of cells into arbitrary clusters.
Single-cell RNA-seq (scRNA-seq) data is often processed to fewer
dimensions using Principal Component Analysis (PCA) and represented in
2-dimensional plots (e.g. t-SNE or UMAP plots). 'singleCellHaystack' uses
Kullback-Leibler divergence to find genes that are expressed in subsets of
cells that are non-randomly positioned in a these multi-dimensional spaces
or 2D representations. For the theoretical background of
'singleCellHaystack' we refer to Vandenbon and Diez (Nature
Communications, 2020) <doi:10.1038/s41467-020-17900-3>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
