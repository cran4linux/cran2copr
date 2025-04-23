%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sgs
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse-Group SLOPE: Adaptive Bi-Level Selection with FDR Control

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SLOPE 
BuildRequires:    R-CRAN-Rlab 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-caret 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-SLOPE 
Requires:         R-CRAN-Rlab 

%description
Implementation of Sparse-group SLOPE (SGS) (Feser and Evangelou (2023)
<doi:10.48550/arXiv.2305.09467>) models. Linear and logistic regression
models are supported, both of which can be fit using k-fold
cross-validation. Dense and sparse input matrices are supported. In
addition, a general Adaptive Three Operator Splitting (ATOS) (Pedregosa
and Gidel (2018) <doi:10.48550/arXiv.1804.02339>) implementation is
provided. Group SLOPE (gSLOPE) (Brzyski et al. (2019)
<doi:10.1080/01621459.2017.1411269>) and group-based OSCAR models (Feser
and Evangelou (2024) <doi:10.48550/arXiv.2405.15357>) are also
implemented. All models are available with strong screening rules (Feser
and Evangelou (2024) <doi:10.48550/arXiv.2405.15357>) for computational
speed-up.

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
