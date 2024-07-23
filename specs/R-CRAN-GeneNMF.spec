%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeneNMF
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Negative Matrix Factorization for Single-Cell Omics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 4.3.0
BuildRequires:    R-CRAN-RcppML 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-lsa 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-Seurat >= 4.3.0
Requires:         R-CRAN-RcppML 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-lsa 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-viridis 

%description
A collection of methods to extract gene programs from single-cell gene
expression data using non-negative matrix factorization (NMF). 'GeneNMF'
contains functions to directly interact with the 'Seurat' toolkit and
derive interpretable gene program signatures.

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
