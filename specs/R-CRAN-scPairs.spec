%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scPairs
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Identifying Synergistic Gene Pairs in Single-Cell and Spatial Transcriptomics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 4.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-SeuratObject 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-Seurat >= 4.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-SeuratObject 
Requires:         R-stats 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-tidyr 

%description
Discovers synergistic gene pairs in single-cell RNA-seq and spatial
transcriptomics data. Unlike conventional pairwise co-expression analyses
that rely on a single correlation metric, scPairs integrates 14
complementary metrics across five orthogonal evidence layers to compute a
composite synergy score with optional permutation-based significance
testing. The five evidence layers span cell-level co-expression (Pearson,
Spearman, biweight midcorrelation, mutual information, ratio consistency),
neighbourhood-aware smoothing (KNN-smoothed correlation, neighbourhood
co-expression, cluster pseudo-bulk, cross-cell-type, neighbourhood
synergy), prior biological knowledge (GO/KEGG co-annotation Jaccard,
pathway bridge score), trans-cellular interaction, and spatial
co-variation (Lee's L, co-location quotient). This multi-scale design
enables researchers to move beyond simple co-expression towards a
comprehensive characterisation of cooperative gene regulation at
transcriptomic and spatial resolution. For more information, see the
package documentation at <https://github.com/zhaoqing-wang/scPairs>.

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
