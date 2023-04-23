%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  penppml
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Poisson Pseudo Maximum Likelihood Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-devtools 

%description
A set of tools that enables efficient estimation of penalized Poisson
Pseudo Maximum Likelihood regressions, using lasso or ridge penalties, for
models that feature one or more sets of high-dimensional fixed effects.
The methodology is based on Breinlich, Corradi, Rocha, Ruta, Santos Silva,
and Zylkin (2021) <http://hdl.handle.net/10986/35451> and takes advantage
of the method of alternating projections of Gaure (2013)
<doi:10.1016/j.csda.2013.03.024> for dealing with HDFE, as well as the
coordinate descent algorithm of Friedman, Hastie and Tibshirani (2010)
<doi:10.18637/jss.v033.i01> for fitting lasso regressions. The package is
also able to carry out cross-validation and to implement the plugin lasso
of Belloni, Chernozhukov, Hansen and Kozbur (2016)
<doi:10.1080/07350015.2015.1102733>.

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
