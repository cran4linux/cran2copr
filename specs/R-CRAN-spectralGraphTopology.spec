%global __brp_check_rpaths %{nil}
%global packname  spectralGraphTopology
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Learning Graphs from Data via Spectral Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen
BuildRequires:    R-CRAN-CVXR
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlist
Requires:         R-CRAN-CVXR

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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
