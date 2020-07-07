%global packname  bikm1
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Co-Clustering Adjusted Rand Index and Bikm1 Procedure forContingency and Binary Data-Sets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grid 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-grid 

%description
Co-clustering of the rows and columns of a contingency or binary matrix,
or double binary matrices and model selection for the number of row and
column clusters. Three models are considered: the Poisson latent block
model for contingency matrix, the binary latent block model for binary
matrix and a new model we develop: the multiple latent block model for
double binary matrices. A new procedure named bikm1 is implemented to
investigate more efficiently the grid of numbers of clusters. Then, the
studied model selection criteria are the integrated completed likelihood
(ICL) and the Bayesian integrated likelihood (BIC). Finally, the
co-clustering adjusted Rand index (CARI) to measure agreement between
co-clustering partitions is implemented. Robert Valerie and Vasseur Yann
(2017) <arXiv:1705.06760>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
