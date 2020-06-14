%global packname  ADPclust
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          2%{?dist}
Summary:          Fast Clustering Using Adaptive Density Peak Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-cluster 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-knitr 

%description
An implementation of ADPclust clustering procedures (Fast Clustering Using
Adaptive Density Peak Detection). The work is built and improved upon the
idea of Rodriguez and Laio (2014)<DOI:10.1126/science.1242072>. ADPclust
clusters data by finding density peaks in a density-distance plot
generated from local multivariate Gaussian density estimation. It includes
an automatic centroids selection and parameter optimization algorithm,
which finds the number of clusters and cluster centroids by comparing
average silhouettes on a grid of testing clustering results; It also
includes a user interactive algorithm that allows the user to manually
selects cluster centroids from a two dimensional "density-distance plot".
Here is the research article associated with this package: "Wang,
Xiao-Feng, and Yifan Xu (2015)<DOI:10.1177/0962280215609948> Fast
clustering using adaptive density peak detection." Statistical methods in
medical research". url:
http://smm.sagepub.com/content/early/2015/10/15/0962280215609948.abstract.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
