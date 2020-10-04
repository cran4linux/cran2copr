%global packname  gama
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Genetic Approach to Maximize Clustering Criterion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ArgumentCheck 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rfast 
Requires:         R-CRAN-ArgumentCheck 
Requires:         R-cluster 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-Rfast 

%description
An evolutionary approach to performing hard partitional clustering. The
algorithm uses genetic operators guided by information about the quality
of individual partitions. The method looks for the best
barycenters/centroids configuration (encoded as real-value) to maximize or
minimize one of the given clustering validation criteria: Silhouette, Dunn
Index, C-Index or Calinski-Harabasz Index. As many other clustering
algorithms, 'gama' asks for k: a fixed a priori established number of
partitions. If the user does not know the best value for k, the algorithm
estimates it by using one of two user-specified options: minimum or broad.
The first method uses an approximation of the second derivative of a set
of points to automatically detect the maximum curvature (the 'elbow') in
the within-cluster sum of squares error (WCSSE) graph. The second method
estimates the best k value through majority voting of 24 indices. One of
the major advantages of 'gama' is to introduce a bias to detect partitions
which attend a particular criterion. References: Scrucca, L. (2013)
<doi:10.18637/jss.v053.i04>; CHARRAD, Malika et al. (2014)
<doi:10.18637/jss.v061.i06>; Tsagris M, Papadakis M. (2018)
<doi:10.7287/peerj.preprints.26605v1>; Kaufman, L., & Rousseeuw, P. (1990,
ISBN:0-47 1-73578-7).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
