%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bsvarSIGNs
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian SVARs with Sign, Zero, and Narrative Restrictions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-bsvars 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bsvars 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-R6 

%description
Implements state-of-the-art algorithms for the Bayesian analysis of
Structural Vector Autoregressions (SVARs) identified by sign, zero, and
narrative restrictions. The core model is based on a flexible Vector
Autoregression with estimated hyper-parameters of the Minnesota prior and
the dummy observation priors as in Giannone, Lenza, Primiceri (2015)
<doi:10.1162/REST_a_00483>. The sign restrictions are implemented
employing the methods proposed by Rubio-Ramírez, Waggoner & Zha (2010)
<doi:10.1111/j.1467-937X.2009.00578.x>, while identification through sign
and zero restrictions follows the approach developed by Arias,
Rubio-Ramírez, & Waggoner (2018) <doi:10.3982/ECTA14468>. Furthermore, our
tool provides algorithms for identification via sign and narrative
restrictions, in line with the methods introduced by Antolín-Díaz and
Rubio-Ramírez (2018) <doi:10.1257/aer.20161852>. Users can also estimate a
model with sign, zero, and narrative restrictions imposed at once. The
package facilitates predictive and structural analyses using impulse
responses, forecast error variance and historical decompositions,
forecasting and conditional forecasting, as well as analyses of structural
shocks and fitted values. All this is complemented by colourful plots,
user-friendly summary functions, and comprehensive documentation including
the vignette by Wang & Woźniak (2024) <doi:10.48550/arXiv.2501.16711>. The
'bsvarSIGNs' package is aligned regarding objects, workflows, and code
structure with the R package 'bsvars' by Woźniak (2024)
<doi:10.32614/CRAN.package.bsvars>, and they constitute an integrated
toolset. It was granted the Di Cook Open-Source Statistical Software Award
by the Statistical Society of Australia in 2024.

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
