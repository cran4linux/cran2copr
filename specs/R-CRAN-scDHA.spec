%global __brp_check_rpaths %{nil}
%global packname  scDHA
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Cell Decomposition using Hierarchical Autoencoder

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-torch >= 0.3.0
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppAnnoy 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-torch >= 0.3.0
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RcppAnnoy 
Requires:         R-methods 
Requires:         R-CRAN-RhpcBLASctl 

%description
Provides a fast and accurate pipeline for single-cell analyses. The
'scDHA' software package can perform clustering, dimension reduction and
visualization, classification, and time-trajectory inference on
single-cell data (Tran et.al. (2021) <DOI:10.1038/s41467-021-21312-2>).

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
