%global packname  HierDpart
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Partitioning Hierarchical Diversity and Differentiation AcrossMetrics and Scales, from Genes to Ecosystems

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-diveRsity 
BuildRequires:    R-CRAN-entropart 
BuildRequires:    R-CRAN-mmod 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hierfstat 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-permute 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-diveRsity 
Requires:         R-CRAN-entropart 
Requires:         R-CRAN-mmod 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hierfstat 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-permute 

%description
Miscellaneous R functions for calculating and decomposing hierarchical
diversity metrics, including hierarchical allele richness, hierarchical
exponential Shannon entropy (true diversity of order q=1), hierarchical
heterozygosity and genetic differentiation (Jaccard dissimilarity, Delta
D,Fst and Jost's D). In addition,a new approach to identify population
structure based on the homogeneity of multivariate variances of Shannon
differentiation is presented. This package allows you to analyse spatial
structured genetic data or species data under a unifying framework
(Gaggiotti, O. E. et al, 2018, Evol Appl, 11:1176-1193;
<DOI:10.1111/eva.12593>), which partitions diversity and differentiation
into any hierarchical levels. It helps you easily structure and format
your data. In summary,it implements the analyses of true diversity
profiles (q=0,1,2), hierarchical diversities and differentiation
decomposition, visualization of population structure, as well as the
estimation of correlation between geographic distance and genetic
differentiation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
