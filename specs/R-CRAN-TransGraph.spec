%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TransGraph
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transfer Graph Learning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-clime 
BuildRequires:    R-CRAN-HeteroGGM 
BuildRequires:    R-CRAN-dcov 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-EvaluationMeasures 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-clime 
Requires:         R-CRAN-HeteroGGM 
Requires:         R-CRAN-dcov 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-EvaluationMeasures 

%description
Transfer learning, aiming to use auxiliary domains to help improve
learning of the target domain of interest when multiple heterogeneous
datasets are available, has been a hot topic in statistical machine
learning. The recent transfer learning methods with statistical guarantees
mainly focus on the overall parameter transfer for supervised models in
the ideal case with the informative auxiliary domains with overall
similarity. In contrast, transfer learning for unsupervised graph learning
is in its infancy and largely follows the idea of overall parameter
transfer as for supervised learning. In this package, the transfer
learning for several complex graphical models is implemented, including
Tensor Gaussian graphical models, non-Gaussian directed acyclic graph
(DAG), and Gaussian graphical mixture models. Notably, this package
promotes local transfer at node-level and subgroup-level in DAG structural
learning and Gaussian graphical mixture models, respectively, which are
more flexible and robust than the existing overall parameter transfer. As
by-products, transfer learning for undirected graphical model (precision
matrix) via D-trace loss, transfer learning for mean vector estimation,
and single non-Gaussian learning via topological layer method are also
included in this package. Moreover, the aggregation of auxiliary
information is an important issue in transfer learning, and this package
provides multiple user-friendly aggregation methods, including sample
weighting, similarity weighting, and most informative selection. (Note:
the transfer for tensor GGM has been temporarily removed in the current
version as its dependent R package Tlasso has been archived. The
historical version TransGraph_1.0.0.tar.gz can be downloaded at
<https://cran.r-project.org/src/contrib/Archive/TransGraph/>) Reference:
Ren, M., Zhen Y., and Wang J. (2024)
<https://jmlr.org/papers/v25/22-1313.html> "Transfer learning for tensor
graphical models". Ren, M., He X., and Wang J. (2023)
<doi:10.48550/arXiv.2310.10239> "Structural transfer learning of
non-Gaussian DAG". Zhao, R., He X., and Wang J. (2022)
<https://jmlr.org/papers/v23/21-1173.html> "Learning linear non-Gaussian
directed acyclic graph with diverging number of nodes".

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
