%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Glarmadillo
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Solve the Graphical Lasso Problem with 'Armadillo'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12
Requires:         R-stats 
Requires:         R-CRAN-RcppArmadillo 

%description
Efficiently implements the Graphical Lasso algorithm, utilizing the
'Armadillo' 'C++' library for rapid computation. This algorithm introduces
an L1 penalty to derive sparse inverse covariance matrices from
observations of multivariate normal distributions. Features include the
generation of random and structured sparse covariance matrices, beneficial
for simulations, statistical method testing, and educational purposes in
graphical modeling. A unique function for regularization parameter
selection based on predefined sparsity levels is also offered, catering to
users with specific sparsity requirements in their models. The methodology
for sparse inverse covariance estimation implemented in this package is
based on the work of Friedman, Hastie, and Tibshirani (2008)
<doi:10.1093/biostatistics/kxm045>.

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
