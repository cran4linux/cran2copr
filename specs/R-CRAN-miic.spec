%global packname  miic
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Learning Causal or Non-Causal Graphical Models Using InformationTheory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-ppcor 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
We report an information-theoretic method which learns a large class of
causal or non-causal graphical models from purely observational data,
while including the effects of unobserved latent variables, commonly found
in many datasets. Starting from a complete graph, the method iteratively
removes dispensable edges, by uncovering significant information
contributions from indirect paths, and assesses edge-specific confidences
from randomization of available data. The remaining edges are then
oriented based on the signature of causality in observational data. This
approach can be applied on a wide range of datasets and provide new
biological insights on regulatory networks from single cell expression
data, genomic alterations during tumor development and co-evolving
residues in protein structures. For more information you can refer to:
Verny et al. Plos Comput Biol. (2017) <doi:10.1371/journal.pcbi.1005662>.

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
