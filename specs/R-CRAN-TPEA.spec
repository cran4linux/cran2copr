%global __brp_check_rpaths %{nil}
%global packname  TPEA
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Novel Topology-Based Pathway Enrichment Analysis Approach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MESS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-MESS 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 
Requires:         R-CRAN-igraph 

%description
We described a novel Topology-based pathway enrichment analysis, which
integrated the global position of the nodes and the topological property
of the pathways in Kyoto Encyclopedia of Genes and Genomes Database. We
also provide some functions to obtain the latest information about
pathways to finish pathway enrichment analysis using this method.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
