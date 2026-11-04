%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panglm
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Models for Panel Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides generalized linear models for panel data, including pooled,
fixed-effects, and random-effects estimators for continuous, binary,
count, ordinal, positive (gamma), and bounded (beta) outcomes, with the
fixed-effects ordered logit of Baetschmann, Staub and Winkelmann (2015)
<doi:10.1111/rssa.12090> and beta regression (Ferrari and Cribari-Neto
2004) <doi:10.1080/0266476042000214501>. Also offers correlated random
effects (Mundlak 1978) <doi:10.2307/1913646>, dynamic models with the
Wooldridge (2005) <doi:10.1002/jae.770> initial conditions solution,
observation weights, average partial effects, regression-spline curves and
linearity tests, difference-in-differences and event studies, and two-part
models for costs (Duan et al. 1983) <doi:10.1080/07350015.1983.10509330>,
including correlated random intercepts (Van Ourti 2004)
<doi:10.1002/hec.920>. Estimators and tests follow standard panel-data
references, including Hausman (1978) <doi:10.2307/1913827>, Chamberlain
(1980) <doi:10.2307/2297110>, Allison and Waterman (2002)
<doi:10.1111/1467-9531.00117>, and Croissant and Millo (2008)
<doi:10.18637/jss.v027.i02>. Core numerical routines are implemented using
'Rcpp', 'RcppArmadillo', and 'RcppParallel'.

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
