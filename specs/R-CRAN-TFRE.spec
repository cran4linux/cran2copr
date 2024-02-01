%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TFRE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tuning-Free Robust and Efficient Approach to High-Dimensional Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-RcppParallel 

%description
Provide functions to estimate the coefficients in high-dimensional linear
regressions via a tuning-free and robust approach. The method was
published in Wang, L., Peng, B., Bradic, J., Li, R. and Wu, Y. (2020), "A
Tuning-free Robust and Efficient Approach to High-dimensional Regression",
Journal of the American Statistical Association, 115:532, 1700-1714(JASA’s
discussion paper), <doi:10.1080/01621459.2020.1840989>. See also Wang, L.,
Peng, B., Bradic, J., Li, R. and Wu, Y. (2020), "Rejoinder to “A
tuning-free robust and efficient approach to high-dimensional regression".
Journal of the American Statistical Association, 115, 1726-1729,
<doi:10.1080/01621459.2020.1843865>; Peng, B. and Wang, L. (2015), "An
Iterative Coordinate Descent Algorithm for High-Dimensional Nonconvex
Penalized Quantile Regression", Journal of Computational and Graphical
Statistics, 24:3, 676-694, <doi:10.1080/10618600.2014.913516>; Clémençon,
S., Colin, I., and Bellet, A. (2016), "Scaling-up empirical risk
minimization: optimization of incomplete u-statistics", The Journal of
Machine Learning Research, 17(1):2682–2717; Fan, J. and Li, R. (2001),
"Variable Selection via Nonconcave Penalized Likelihood and its Oracle
Properties", Journal of the American Statistical Association, 96:456,
1348-1360, <doi:10.1198/016214501753382273>.

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
