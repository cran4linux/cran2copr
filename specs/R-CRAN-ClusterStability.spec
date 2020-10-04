%global packname  ClusterStability
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Assessment of Stability of Individual Objects or Clusters inPartitioning Solutions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.4
Requires:         R-core >= 2.2.4
BuildRequires:    R-CRAN-copula >= 0.999
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-WeightedCluster 
Requires:         R-CRAN-copula >= 0.999
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-clusterCrit 
Requires:         R-cluster 
Requires:         R-CRAN-WeightedCluster 

%description
Allows one to assess the stability of individual objects, clusters and
whole clustering solutions based on repeated runs of the K-means and
K-medoids partitioning algorithms.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
