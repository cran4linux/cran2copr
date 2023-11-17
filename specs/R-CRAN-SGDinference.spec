%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SGDinference
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inference with Stochastic Gradient Descent

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-stats 

%description
Estimation and inference methods for large-scale mean and quantile
regression models via stochastic (sub-)gradient descent (S-subGD)
algorithms. The inference procedure handles cross-sectional data
sequentially: (i) updating the parameter estimate with each incoming "new
observation", (ii) aggregating it as a Polyak-Ruppert average, and (iii)
computing an asymptotically pivotal statistic for inference through random
scaling. The methodology used in the 'SGDinference' package is described
in detail in the following papers: (i) Lee, S., Liao, Y., Seo, M.H. and
Shin, Y. (2022) <doi:10.1609/aaai.v36i7.20701> "Fast and robust online
inference with stochastic gradient descent via random scaling". (ii) Lee,
S., Liao, Y., Seo, M.H. and Shin, Y. (2023) <arXiv:2209.14502> "Fast
Inference for Quantile Regression with Tens of Millions of Observations".

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
