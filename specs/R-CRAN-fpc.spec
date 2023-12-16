%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fpc
%global packver   2.2-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.11
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Procedures for Clustering

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-prabclus 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-prabclus 
Requires:         R-CRAN-class 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-kernlab 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 

%description
Various methods for clustering and cluster validation. Fixed point
clustering. Linear regression clustering. Clustering by merging Gaussian
mixture components. Symmetric and asymmetric discriminant projections for
visualisation of the separation of groupings. Cluster validation
statistics for distance based clustering including corrected Rand index.
Standardisation of cluster validation statistics by random clusterings and
comparison between many clustering methods and numbers of clusters based
on this. Cluster-wise cluster stability assessment. Methods for estimation
of the number of clusters: Calinski-Harabasz, Tibshirani and Walther's
prediction strength, Fang and Wang's bootstrap stability.
Gaussian/multinomial mixture fitting for mixed continuous/categorical
variables. Variable-wise statistics for cluster interpretation. DBSCAN
clustering. Interface functions for many clustering methods implemented in
R, including estimating the number of clusters with kmeans, pam and clara.
Modality diagnosis for Gaussian mixtures. For an overview see package?fpc.

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
