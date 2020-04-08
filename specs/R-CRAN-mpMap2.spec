%global packname  mpMap2
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Genetic Analysis of Multi-Parent Recombinant Inbred Lines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-car 

%description
Constructing linkage maps, reconstructing haplotypes, estimating linkage
disequilibrium and quantitative trait loci (QTL) mapping in multi-parent
Recombinant Inbred Lines designs.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/generateDatasets
%doc %{rlibdir}/%{packname}/mathematica
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
