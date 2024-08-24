%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssMRCD
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Smoothed MRCD Estimator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-rootSolve 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-reshape2 

%description
Estimation of the Spatially Smoothed Minimum Regularized Determinant
(ssMRCD) estimator and its usage in an ssMRCD-based outlier detection
method as described in Puchhammer and Filzmoser (2023)
<doi:10.1080/10618600.2023.2277875> and for sparse robust PCA for
multi-source data described in Puchhammer, Wilms and Filzmoser (2024)
<doi:10.48550/arXiv.2407.16299>. Included are also complementary
visualization and parameter tuning tools.

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
