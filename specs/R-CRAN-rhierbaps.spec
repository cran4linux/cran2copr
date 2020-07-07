%global packname  rhierbaps
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Clustering Genetic Sequence Data Using the HierBAPS Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-patchwork 

%description
Implements the hierarchical Bayesian analysis of populations structure
(hierBAPS) algorithm of Cheng et al. (2013) <doi:10.1093/molbev/mst028>
for clustering DNA sequences from multiple sequence alignments in FASTA
format. The implementation includes improved defaults and plotting
capabilities and unlike the original 'MATLAB' version removes singleton
SNPs by default.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vignette-supp
%{rlibdir}/%{packname}/INDEX
