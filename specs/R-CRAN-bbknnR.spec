%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bbknnR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Batch Balanced KNN in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-uwot >= 0.1.14
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppAnnoy 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-SeuratObject 
BuildRequires:    R-CRAN-tidytable 
Requires:         R-CRAN-uwot >= 0.1.14
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-RcppAnnoy 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-SeuratObject 
Requires:         R-CRAN-tidytable 

%description
A fast and intuitive batch effect removal tool for single-cell data. BBKNN
is originally used in the 'scanpy' python package, and now can be used
with 'Seurat' seamlessly.

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
