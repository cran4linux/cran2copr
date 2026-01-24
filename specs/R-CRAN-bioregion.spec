%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bioregion
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comparison of Bioregionalization Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-fastkmedoids 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-rcartocolor 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-fastkmedoids 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-rcartocolor 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
The main purpose of this package is to propose a transparent
methodological framework to compare bioregionalization methods based on
hierarchical and non-hierarchical clustering algorithms (Kreft & Jetz
(2010) <doi:10.1111/j.1365-2699.2010.02375.x>) and network algorithms
(Lenormand et al. (2019) <doi:10.1002/ece3.4718> and Leroy et al. (2019)
<doi:10.1111/jbi.13674>).

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
