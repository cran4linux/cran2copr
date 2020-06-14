%global packname  hypervolume
%global packver   2.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.12
Release:          2%{?dist}
Summary:          High Dimensional Geometry and Set Operations Using KernelDensity Estimation, Support Vector Machines, and Convex Hulls

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-hitandrun 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-maps 
Requires:         R-MASS 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-hitandrun 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 

%description
Estimates the shape and volume of high-dimensional datasets and performs
set operations: intersection / overlap, union, unique components,
inclusion test, and hole detection. Uses stochastic geometry approach to
high-dimensional kernel density estimation, support vector machine
delineation, and convex hull generation. Applications include modeling
trait and niche hypervolumes and species distribution modeling.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
