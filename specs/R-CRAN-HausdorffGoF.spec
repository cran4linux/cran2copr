%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HausdorffGoF
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          One- And Two-Sample Hausdorff Goodness-of-Fit Test

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-KSgeneral 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-KSgeneral 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Computes the test statistic and p-values of the one-sample and two-sample
Hausdorff (H) goodness-of-fit tests. The H statistic measures the
Hausdorff distance under the Chebyshev (l-infinity) metric, between the
two cumulative distribution functions (cdfs) underlying the corresponding
one-sample and two-sample null hypothesis. It coincides to the side length
of the largest axis-aligned square (hypercube) that can be inscribed
between the two cdfs. The following cases are covered: (i) one-sample,
univariate; (ii) two-sample univariate; and (iii) two-sample bivariate.
Exact one-sample p-values are computed in O(n^2 log n) time via the
'Exact-KS-FFT' method of Dimitrova, Kaishev, and Tan (2020)
<doi:10.18637/jss.v095.i10>; two-sample p-values are obtained by
permutation. A key advantage of the H test is that its sensitivity can be
directed towards the left tail, body, or right tail of the distribution by
tuning a scale parameter sigma, and therefore maximizing its power which
as shown numerically is significantly higher than the power of the
classical tests such as the Kolmogorov-Smirnov, Cramer-von Mises, and
Anderson-Darling test, especially when the right tail of the distribution
is targeted. The sensitivity of the test (left tail, body, or right tail)
is governed by two parameters psi1 and psi2, whose values needs to be
input. Then the optimal value of the scale parameter sigma is
automatically computed.

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
