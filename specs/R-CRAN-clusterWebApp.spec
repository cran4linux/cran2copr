%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusterWebApp
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Universal Clustering Analysis Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-factoextra 
Requires:         R-datasets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-magrittr 

%description
An interactive platform for clustering analysis and teaching based on the
'shiny' web application framework. Supports multiple popular clustering
algorithms including k-means, hierarchical clustering, DBSCAN
(Density-Based Spatial Clustering of Applications with Noise), PAM
(Partitioning Around Medoids), GMM (Gaussian Mixture Model), and spectral
clustering. Users can upload datasets or use built-in ones, visualize
clustering results using dimensionality reduction methods such as
Principal Component Analysis (PCA) and t-distributed Stochastic Neighbor
Embedding (t-SNE), evaluate clustering quality via silhouette plots, and
explore method-specific visualizations and guides. For details on
implemented methods, see: Reynolds (2009, ISBN:9781598296975) for GMM;
Luxburg (2007) <doi:10.1007/s11222-007-9033-z> for spectral clustering.

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
