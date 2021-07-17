%global __brp_check_rpaths %{nil}
%global packname  bikm1
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Co-Clustering Adjusted Rand Index and Bikm1 Procedure for Contingency and Binary Data-Sets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-grid 
Requires:         R-CRAN-lpSolve 

%description
Co-clustering of the rows and columns of a contingency or binary matrix,
or double binary matrices and model selection for the number of row and
column clusters. Three models are considered: the Poisson latent block
model for contingency matrix, the binary latent block model for binary
matrix and a new model we develop: the multiple latent block model for
double binary matrices. A new procedure named bikm1 is implemented to
investigate more efficiently the grid of numbers of clusters. Then, the
studied model selection criteria are the integrated completed likelihood
(ICL) and the Bayesian integrated likelihood (BIC). Finally, the
co-clustering adjusted Rand index (CARI) to measure agreement between
co-clustering partitions is implemented. Robert Valerie, Vasseur Yann,
Brault Vincent (2021) <doi:10.1007/s00357-020-09379-w>.

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
