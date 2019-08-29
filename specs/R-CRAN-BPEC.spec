%global packname  BPEC
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Bayesian Phylogeographic and Ecological Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-OpenStreetMap 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-CRAN-OpenStreetMap 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ape 

%description
Model-based clustering for phylogeographic data comprising mtDNA sequences
and geographical locations along with optional environmental
characteristics, aiming to identify migration events that led to
homogeneous population clusters.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/coordsLocsFile.txt
%doc %{rlibdir}/%{packname}/haplotypes.nex
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
