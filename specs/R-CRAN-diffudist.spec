%global __brp_check_rpaths %{nil}
%global packname  diffudist
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diffusion Distance for Complex Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-viridis 

%description
Enables the evaluation of diffusion distances for complex single-layer
networks. Given a network one can define different types of Laplacian (or
transition) matrices corresponding to different continuous-time random
walks dynamics on the network. This package enables the evaluation of
Laplacians, stochastic matrices, and the corresponding diffusion distance
matrices. The metric structure induced by the network-driven process is
richer and more robust than the one given by shortest-paths and allows to
study the geometry induced by different types of diffusion-like
communication mechanisms taking place on complex networks. For more
details see: De Domenico, M. (2017) <doi:10.1103/physrevlett.118.168301>
and Bertagnolli, G. and De Domenico, M. (2021)
<doi:10.1103/PhysRevE.103.042301>.

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
