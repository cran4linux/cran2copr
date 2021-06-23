%global __brp_check_rpaths %{nil}
%global packname  segmenTier
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Similarity-Based Segmentation of Multidimensional Signals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-Rcpp >= 0.12.7

%description
A dynamic programming solution to segmentation based on maximization of
arbitrary similarity measures within segments. The general idea, theory
and this implementation are described in Machne, Murray & Stadler (2017)
<doi:10.1038/s41598-017-12401-8>. In addition to the core algorithm, the
package provides time-series processing and clustering functions as
described in the publication. These are generally applicable where a
`k-means` clustering yields meaningful results, and have been specifically
developed for clustering of the Discrete Fourier Transform of periodic
gene expression data (`circadian' or `yeast metabolic oscillations'). This
clustering approach is outlined in the supplemental material of Machne &
Murray (2012) <doi:10.1371/journal.pone.0037906>), and here is used as a
basis of segment similarity measures. Notably, the time-series processing
and clustering functions can also be used as stand-alone tools,
independent of segmentation, e.g., for transcriptome data already mapped
to genes.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
