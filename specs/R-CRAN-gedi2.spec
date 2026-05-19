%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gedi2
%global packver   2.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Gene Expression Decomposition and Integration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
A memory-efficient implementation for integrating gene expression data
from single-cell RNA sequencing experiments. Uses a C++ backend with thin
R wrappers to enable analysis of large-scale single-cell datasets. The
package supports multiple data modalities including count matrices, paired
data (splicing, RNA velocity, CITE-seq), and binary indicators. It
implements a latent variable model with block coordinate descent
optimization for dimensionality reduction and batch effect correction.
Core algorithms are described in Madrigal et al. (2024)
<doi:10.1038/s41467-024-50963-0>.

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
