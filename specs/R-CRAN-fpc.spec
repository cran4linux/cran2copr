%global packname  fpc
%global packver   2.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.6
Release:          1%{?dist}
Summary:          Flexible Procedures for Clustering

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-prabclus 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-MASS 
Requires:         R-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-prabclus 
Requires:         R-class 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
