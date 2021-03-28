%global packname  doc2vec
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distributed Representations of Sentences, Documents and Topics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-stats 
Requires:         R-utils 

%description
Learn vector representations of sentences, paragraphs or documents by
using the 'Paragraph Vector' algorithms, namely the distributed bag of
words ('PV-DBOW') and the distributed memory ('PV-DM') model. The
techniques in the package are detailed in the paper "Distributed
Representations of Sentences and Documents" by Mikolov et al. (2014),
available at <arXiv:1405.4053>. The package also provides an
implementation to cluster documents based on these embedding using a
technique called top2vec. Top2vec finds clusters in text documents by
combining techniques to embed documents and words and density-based
clustering. It does this by embedding documents in the semantic space as
defined by the 'doc2vec' algorithm. Next it maps these document embeddings
to a lower-dimensional space using the 'Uniform Manifold Approximation and
Projection' (UMAP) clustering algorithm and finds dense areas in that
space using a 'Hierarchical Density-Based Clustering' technique (HDBSCAN).
These dense areas are the topic clusters which can be represented by the
corresponding topic vector which is an aggregate of the document
embeddings of the documents which are part of that topic cluster. In the
same semantic space similar words can be found which are representative of
the topic. More details can be found in the paper 'Top2Vec: Distributed
Representations of Topics' by D. Angelov available at <arXiv:2008.09470>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
