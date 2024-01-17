%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuantRegGLasso
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptively Weighted Group Lasso for Semiparametric Quantile Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-ggplot2 

%description
Implements an adaptively weighted group Lasso procedure for simultaneous
variable selection and structure identification in varying coefficient
quantile regression models and additive quantile regression models with
ultra-high dimensional covariates. The methodology, grounded in a strong
sparsity condition, establishes selection consistency under certain weight
conditions. To address the challenge of tuning parameter selection in
practice, a BIC-type criterion named high-dimensional information
criterion (HDIC) is proposed. The Lasso procedure, guided by
HDIC-determined tuning parameters, maintains selection consistency.
Theoretical findings are strongly supported by simulation studies. (Toshio
Honda, Ching-Kang Ing, Wei-Ying Wu, 2019, <DOI:10.3150/18-BEJ1091>).

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
