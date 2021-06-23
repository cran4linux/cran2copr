%global __brp_check_rpaths %{nil}
%global packname  spectralGraphTopology
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Learning Graphs from Data via Spectral Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlist 

%description
In the era of big data and hyperconnectivity, learning high-dimensional
structures such as graphs from data has become a prominent task in machine
learning and has found applications in many fields such as finance, health
care, and networks. 'spectralGraphTopology' is an open source, documented,
and well-tested R package for learning graphs from data. It provides
implementations of state of the art algorithms such as Combinatorial Graph
Laplacian Learning (CGL), Spectral Graph Learning (SGL), Graph Estimation
based on Majorization-Minimization (GLE-MM), and Graph Estimation based on
Alternating Direction Method of Multipliers (GLE-ADMM). In addition, graph
learning has been widely employed for clustering, where specific
algorithms are available in the literature. To this end, we provide an
implementation of the Constrained Laplacian Rank (CLR) algorithm.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
