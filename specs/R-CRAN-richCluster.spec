%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  richCluster
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast, Robust Clustering Algorithms for Gene Enrichment Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-heatmaply 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-heatmaply 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-plotly 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 

%description
Clusters functionally related biological terms from gene set enrichment
results. Terms are compared by the overlap of their gene sets using
Cohen's kappa, the Jaccard index, or the Dice coefficient, and the
resulting similarity matrix is grouped either by agglomerative
hierarchical clustering with single, complete, average, or Ward linkage,
or by the seed-and-merge procedure of the 'DAVID' functional
classification tool. The distance and clustering routines are written in
'C++' for speed. The methods are described in Huang et al. (2007)
<doi:10.1186/gb-2007-8-9-r183>, Ward (1963)
<doi:10.1080/01621459.1963.10500845>, Cohen (1960)
<doi:10.1177/001316446002000104>, and Jaccard (1912)
<doi:10.1111/j.1469-8137.1912.tb05611.x>.

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
