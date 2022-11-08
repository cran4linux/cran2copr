%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SeuratObject
%global packver   4.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Data Structures for Single Cell Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-sp >= 1.5.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-sp >= 1.5.0
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Defines S4 classes for single-cell genomic data and associated
information, such as dimensionality reduction embeddings, nearest-neighbor
graphs, and spatially-resolved coordinates. Provides data access methods
and R-native hooks to ensure the Seurat object is familiar to other R
users. See Satija R, Farrell J, Gennert D, et al (2015)
<doi:10.1038/nbt.3192>, Macosko E, Basu A, Satija R, et al (2015)
<doi:10.1016/j.cell.2015.05.002>, and Stuart T, Butler A, et al (2019)
<doi:10.1016/j.cell.2019.05.031> for more details.

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
