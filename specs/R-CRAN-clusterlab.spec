%global packname  clusterlab
%global packver   0.0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2.7
Release:          1%{?dist}
Summary:          Flexible Gaussian Cluster Simulator

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape 

%description
Clustering is a central task in big data analyses and clusters are often
Gaussian or near Gaussian. However, a flexible Gaussian cluster simulation
tool with precise control over the size, variance, and spacing of the
clusters in NXN dimensional space does not exist. This is why we created
'clusterlab'. The algorithm first creates X points equally spaced on the
circumference of a circle in 2D space. These form the centers of each
cluster to be simulated. Additional samples are added by adding Gaussian
noise to each cluster center and concatenating the new sample
co-ordinates. Then if the feature space is greater than 2D, the generated
points are considered principal component scores and projected into N
dimensional space using linear combinations using fixed eigenvectors.
Through using vector rotations and scalar multiplication clusterlab can
generate complex patterns of Gaussian clusters and outliers.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
