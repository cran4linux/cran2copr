%global packname  flexclust
%global packver   1.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Flexible Cluster Algorithms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-class 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-CRAN-modeltools 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-class 

%description
The main function kcca implements a general framework for k-centroids
cluster analysis supporting arbitrary distance measures and centroid
computation. Further cluster methods include hard competitive learning,
neural gas, and QT clustering. There are numerous visualization methods
for cluster results (neighborhood graphs, convex cluster hulls, barcharts
of centroids, ...), and bootstrap methods for the analysis of cluster
stability.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
