%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  intrinsicFRP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Oracle Estimation and Inference for Tradable Factor Risk Premia

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Tradable factor risk premia are given by the negative factor covariance
with the Stochastic Discount Factor projection on returns. This package
provides efficient computation of tradable and Oracle tradable factor risk
premia estimators and their standard errors; see A. Quaini, F. Trojani and
M. Yuan (2023)
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4574683>. Tradable
factor risk premia are robust to misspecification or weak identification
in asset pricing models, and they are zero for any factor weakly
correlated with returns. Their Oracle estimator performs as well as if the
weak or useless factors were known in advance. This means it not only
consistently removes useless factors and factors weakly correlated with
returns but also gives rise to reliable tests of asset pricing models.

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
