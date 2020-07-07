%global packname  liger
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Lightweight Iterative Geneset Enrichment

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixStats 
Requires:         R-parallel 

%description
Gene Set Enrichment Analysis (GSEA) is a computational method that
determines whether an a priori defined set of genes shows statistically
significant, concordant differences between two biological states. The
original algorithm is detailed in Subramanian et al. with 'Java'
implementations available through the Broad Institute (Subramanian et al.
2005 <doi:10.1073/pnas.0506580102>). The 'liger' package provides a
lightweight R implementation of this enrichment test on a list of values
(Fan et al., 2017 <doi:10.5281/zenodo.887386>). Given a list of values,
such as p-values or log-fold changes derived from differential expression
analysis or other analyses comparing biological states, this package
enables you to test a priori defined set of genes for enrichment to enable
interpretability of highly significant or high fold-change genes.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
