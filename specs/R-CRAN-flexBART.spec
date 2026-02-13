%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexBART
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          A More Flexible BART Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glmnet >= 4.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-methods 

%description
Implements a faster and more expressive version of Bayesian Additive
Regression Trees that, at a high level, approximates unknown functions as
a weighted sum of binary regression tree ensembles. Supports fitting
(generalized) linear varying coefficient models that posits a linear
relationship between the inverse link and some covariates but allows that
relationship to change as a function of other covariates. Additionally
supports fitting heteroscedastic BART models, in which both the mean and
log-variance are approximated with separate regression tree ensembles. A
formula interface allows for different splitting variables to be used in
each ensemble. For more details see Deshpande (2025)
<doi:10.1080/10618600.2024.2431072> and Deshpande et al. (2024)
<doi:10.1214/24-BA1470>.

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
