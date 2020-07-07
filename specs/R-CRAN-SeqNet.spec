%global packname  SeqNet
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Generate RNA-Seq Data from Gene-Gene Association Networks

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Methods to generate random gene-gene association networks and simulate
RNA-seq data from them. Includes functions to generate random networks of
any size and perturb them to obtain differential networks. Network objects
are built from individual, overlapping modules that represent pathways.
The resulting network has various topological properties that are
characteristic of gene regulatory networks. RNA-seq data can be generated
such that the association among gene expression profiles reflect the
underlying network. A reference RNA-seq dataset can be provided to model
realistic marginal distributions. Plotting functions are available to
visualize a network, compare two networks, and compare the expression of
two genes across multiple networks.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
