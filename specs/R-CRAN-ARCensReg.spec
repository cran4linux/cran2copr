%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARCensReg
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Univariate Censored Linear Regression Model with Autoregressive Errors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-qqplotr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-qqplotr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-utils 

%description
It fits a univariate left, right, or interval censored linear regression
model with autoregressive errors, considering the normal or the Student-t
distribution for the innovations. It provides estimates and standard
errors of the parameters, predicts future observations, and supports
missing values on the dependent variable. References used for this
package: Schumacher, F. L., Lachos, V. H., & Dey, D. K. (2017). Censored
regression models with autoregressive errors: A likelihood-based
perspective. Canadian Journal of Statistics, 45(4), 375-392
<doi:10.1002/cjs.11338>. Schumacher, F. L., Lachos, V. H., Vilca-Labra, F.
E., & Castro, L. M. (2018). Influence diagnostics for censored regression
models with autoregressive errors. Australian & New Zealand Journal of
Statistics, 60(2), 209-229 <doi:10.1111/anzs.12229>. Valeriano, K. A.,
Schumacher, F. L., Galarza, C. E., & Matos, L. A. (2024). Censored
autoregressive regression models with Student‐t innovations. Canadian
Journal of Statistics, 52(3), 804-828 <doi:10.1002/cjs.11804>.

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
