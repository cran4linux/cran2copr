%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ProjectionBasedClustering
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Projection Based Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-GeneralizedUmatrix 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-GeneralizedUmatrix 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-plotly 
Requires:         R-grDevices 

%description
A clustering approach applicable to every projection method is proposed
here. The two-dimensional scatter plot of any projection method can
construct a topographic map which displays unapparent data structures by
using distance and density information of the data. The generalized
U*-matrix renders this visualization in the form of a topographic map,
which can be used to automatically define the clusters of high-dimensional
data. The whole system is based on Thrun and Ultsch, "Using Projection
based Clustering to Find Distance and Density based Clusters in
High-Dimensional Data" <DOI:10.1007/s00357-020-09373-2>. Selecting the
correct projection method will result in a visualization in which
mountains surround each cluster. The number of clusters can be determined
by counting valleys on the topographic map. Most projection methods are
wrappers for already available methods in R. By contrast, the neighbor
retrieval visualizer (NeRV) is based on C++ source code of the 'dredviz'
software package, the t-SNE multicore version is based on C++ source code
of Dmitry Ulyanov, and the Curvilinear Component Analysis (CCA) is
translated from 'MATLAB' ('SOM Toolbox' 2.0) to R.

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
