%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbscan
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Density-Based Spatial Clustering of Applications with Noise (DBSCAN) and Related Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-stats 

%description
A fast reimplementation of several density-based algorithms of the DBSCAN
family. Includes the clustering algorithms DBSCAN (density-based spatial
clustering of applications with noise) and HDBSCAN (hierarchical DBSCAN),
the ordering algorithm OPTICS (ordering points to identify the clustering
structure), shared nearest neighbor clustering, and the outlier detection
algorithms LOF (local outlier factor) and GLOSH (global-local outlier
score from hierarchies). The implementations use the kd-tree data
structure (from library ANN) for faster k-nearest neighbor search. An R
interface to fast kNN and fixed-radius NN search is also provided.
Hahsler, Piekenbrock and Doran (2019) <doi:10.18637/jss.v091.i01>.

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
