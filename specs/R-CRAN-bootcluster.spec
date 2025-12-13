%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootcluster
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrapping Estimates of Clustering Stability

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.1
Requires:         R-core >= 3.5.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust >= 5.0.0
BuildRequires:    R-CRAN-igraph >= 1.2.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-mclust >= 5.0.0
Requires:         R-CRAN-igraph >= 1.2.0
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-network 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-progress 

%description
Implementation of the bootstrapping approach for the estimation of
clustering stability and its application in estimating the number of
clusters, as introduced by Yu et al
(2016)<doi:10.1142/9789814749411_0007>. Implementation of the
non-parametric bootstrap approach to assessing the stability of module
detection in a graph, the extension for the selection of a parameter set
that defines a graph from data in a way that optimizes stability and the
corresponding visualization functions, as introduced by Tian et al (2021)
<doi:10.1002/sam.11495>. Implemented out-of-bag stability estimation
function and k-select Smin-based k-selection function as introduced by Liu
et al (2022) <doi:10.1002/sam.11593>. Implemented ensemble clustering
method based-on k-means clustering method, spectral clustering method and
hierarchical clustering method.

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
