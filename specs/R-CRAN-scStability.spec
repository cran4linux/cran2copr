%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scStability
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring the Stability of Dimension Reduction and Cluster Assignment in scRNA-Seq Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aricode 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-aricode 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-Seurat 
Requires:         R-stats 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-vegan 

%description
Provides functions for evaluating the stability of low-dimensional
embeddings and cluster assignments in single‑cell RNA sequencing
(scRNA‑seq) datasets. Starting from a principal component analysis (PCA)
object, users can generate multiple replicates of t‑Distributed Stochastic
Neighbor Embedding (t‑SNE) or Uniform Manifold Approximation and
Projection (UMAP) embeddings. Embedding stability is quantified by
computing pairwise Kendall’s Tau correlations across replicates and
summarizing the distribution of correlation coefficients. In addition to
dimensionality reduction, 'scStability' assesses clustering consistency
using either Louvain or Leiden algorithms and calculating the Normalized
Mutual Information (NMI) between all pairs of cluster assignments. For
background on UMAP and t-SNE algorithms, see McInnes et al. (2020,
<doi:10.21105/joss.00861>) and van der Maaten & Hinton (2008,
<https://lvdmaaten.github.io/tsne/>), respectively.

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
