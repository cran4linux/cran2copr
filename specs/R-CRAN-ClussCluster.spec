%global __brp_check_rpaths %{nil}
%global packname  ClussCluster
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Simultaneous Detection of Clusters and Cluster-Specific Genes inHigh-Throughput Transcriptome Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-VennDiagram 
Requires:         R-stats >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-VennDiagram 

%description
Implements a new method 'ClussCluster' descried in Ge Jiang and Jun Li,
"Simultaneous Detection of Clusters and Cluster-Specific Genes in
High-throughput Transcriptome Data" (Unpublished). Simultaneously perform
clustering analysis and signature gene selection on high-dimensional
transcriptome data sets.  To do so, 'ClussCluster' incorporates a
Lasso-type regularization penalty term to the objective function of K-
means so that cell-type-specific signature genes can be identified while
clustering the cells.

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
