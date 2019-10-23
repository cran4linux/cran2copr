%global packname  Seurat
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}
Summary:          Tools for Single Cell Genomics

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-Matrix >= 1.2.14
BuildRequires:    R-CRAN-leiden >= 0.3.1
BuildRequires:    R-CRAN-sctransform >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-metap 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppAnnoy 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tsne 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-Matrix >= 1.2.14
Requires:         R-CRAN-leiden >= 0.3.1
Requires:         R-CRAN-sctransform >= 0.2.0
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-cluster 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggridges 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-irlba 
Requires:         R-KernSmooth 
Requires:         R-CRAN-lmtest 
Requires:         R-MASS 
Requires:         R-CRAN-metap 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-png 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-RcppAnnoy 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-rsvd 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-SDMTools 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-tsne 
Requires:         R-utils 
Requires:         R-CRAN-uwot 

%description
A toolkit for quality control, analysis, and exploration of single cell
RNA sequencing data. 'Seurat' aims to enable users to identify and
interpret sources of heterogeneity from single cell transcriptomic
measurements, and to integrate diverse types of single cell data. See
Satija R, Farrell J, Gennert D, et al (2015) <doi:10.1038/nbt.3192>,
Macosko E, Basu A, Satija R, et al (2015)
<doi:10.1016/j.cell.2015.05.002>, and Butler A and Satija R (2017)
<doi:10.1101/164889> for more details.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
