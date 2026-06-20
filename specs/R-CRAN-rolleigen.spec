%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rolleigen
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rolling Eigenanalysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-roll >= 1.1.7
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 

%description
Fast and efficient computation of rolling and expanding eigenanalysis for
time-series data. The 'rolleigen' package decomposes the covariance matrix
of the explanatory variables into eigenvalues and eigenvectors to perform
principal component analysis (Pearson, 1901,
<doi:10.1080/14786440109462720>; Hotelling, 1933, <doi:10.1037/h0071325>)
and principal component regression (Massy, 1965,
<doi:10.1080/01621459.1965.10480787>) over rolling and expanding windows.
For each window, the eigenvalues and eigenvectors are computed from the
covariance matrix and, optionally, ordered from largest to smallest to
summarize the directions of greatest variation in the data. A subset of
leading components is then used to fit a regression that mitigates
collinearity in the explanatory variables. Use cases include
dimensionality reduction, factor extraction, and regression on collinear
explanatory variables. The package supports rolling and expanding windows,
weights, and handling of missing values via the min_obs, complete_obs, and
na_restore arguments. The implementation uses the online and offline
algorithms from the 'roll' package to compute rolling and expanding
cross-products efficiently, with parallelism across columns and windows
provided by 'RcppParallel'.

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
