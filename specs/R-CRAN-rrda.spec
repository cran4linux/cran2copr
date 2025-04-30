%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rrda
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ridge Redundancy Analysis for High-Dimensional Omics Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Efficient framework for ridge redundancy analysis (rrda), tailored for
high-dimensional omics datasets where the number of predictors exceeds the
number of samples. The method leverages Singular Value Decomposition (SVD)
to avoid direct inversion of the covariance matrix, enhancing scalability
and performance. It also introduces a memory-efficient storage strategy
for coefficient matrices, enabling practical use in large-scale
applications. The package supports cross-validation for selecting
regularization parameters and reduced-rank dimensions, making it a robust
and flexible tool for multivariate analysis in omics research. Please
refer to our article (Yoshioka et al., 2025) for more details.

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
