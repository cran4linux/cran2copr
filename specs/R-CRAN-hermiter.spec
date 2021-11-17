%global __brp_check_rpaths %{nil}
%global packname  hermiter
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Sequential and Batch Estimation of Univariate and Bivariate Probability Density Functions and Cumulative Distribution Functions along with Quantiles (Univariate) and Spearman's Correlation (Bivariate)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-methods 

%description
Facilitates estimation of full univariate and bivariate probability
density functions and cumulative distribution functions along with full
quantile functions (univariate) and nonparametric correlation (bivariate)
using Hermite series based estimators. These estimators are particularly
useful in the sequential setting (both stationary and non-stationary) and
one-pass batch estimation setting for large data sets. Based on:
Stephanou, Michael, Varughese, Melvin and Macdonald, Iain. "Sequential
quantiles via Hermite series density estimation." Electronic Journal of
Statistics 11.1 (2017): 570-607 <doi:10.1214/17-EJS1245>, Stephanou,
Michael and Varughese, Melvin. "On the properties of Hermite series based
distribution function estimators." Metrika (2020)
<doi:10.1007/s00184-020-00785-z> and Stephanou, Michael and Varughese,
Melvin. "Sequential estimation of Spearman rank correlation using Hermite
series estimators." Journal of Multivariate Analysis (2021)
<doi:10.1016/j.jmva.2021.104783>.

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
