%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMgaussian
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Expectation-Maximization Algorithm for Multivariate Normal (Gaussian) with Missing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glassoFast 
Requires:         R-CRAN-caret 

%description
Initially designed to distribute code for estimating the Gaussian
graphical model with Lasso regularization, also known as the graphical
lasso (glasso), using an Expectation-Maximization (EM) algorithm based on
work by Städler and Bühlmann (2012) <doi:10.1007/s11222-010-9219-7>. As a
byproduct, code for estimating means and covariances (or the precision
matrix) under a multivariate normal (Gaussian) distribution is also
available.

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
