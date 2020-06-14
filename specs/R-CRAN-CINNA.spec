%global packname  CINNA
%global packver   1.1.53
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.53
Release:          2%{?dist}
Summary:          Deciphering Central Informative Nodes in Network Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-centiserve 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-qdapTools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-intergraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-centiserve 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-qdapTools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-intergraph 

%description
Functions for computing, comparing and demonstrating top informative
centrality measures within a network.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
