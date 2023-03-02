%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RaceID
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Identification of Cell Types and Inference of Lineage Trees from Single-Cell RNA-Seq Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-coop 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-FateID 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-harmony 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-leiden 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-runner 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-coop 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-FateID 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-harmony 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-leiden 
Requires:         R-CRAN-locfit 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-parallel 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-princurve 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-runner 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-vegan 

%description
Application of 'RaceID' allows inference of cell types and prediction of
lineage trees by he StemID2 algorithm. Herman, J.S., Sagar, Grün D. (2018)
<DOI:10.1038/nmeth.4662>.

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
