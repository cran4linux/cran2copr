%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manifoldsR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Low-Dimensional Embeddings and Clustering via 'Rust'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
R interface to the Rust crates 'manifolds-rs', 'ann-search-rs' and
'evoc-rs'. Builds 2D (or higher) embeddings with UMAP (McInnes et al.,
2018) <doi:10.48550/arXiv.1802.03426>, t-SNE (van der Maaten and Hinton,
2008) <https://jmlr.org/papers/v9/vandermaaten08a.html>, densMAP and
den-SNE (Narayan et al., 2021) <doi:10.1038/s41587-020-00801-7>, PHATE
(Moon et al., 2019) <doi:10.1038/s41587-019-0336-3>, PaCMAP (Wang et al.,
2021) <https://jmlr.org/papers/v22/20-1061.html>, ForceAtlas2 (Jacomy et
al., 2014) <doi:10.1371/journal.pone.0098679>, DREAMS and diffusion maps.
Also generates approximate nearest neighbour graphs that every method can
reuse, plus EVoC and k-means clustering. Multi-threaded via 'Rayon', with
f32 or f64 precision.

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
