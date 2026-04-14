%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lgspline
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lagrangian Multiplier Smoothing Splines for Smooth Function Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-quadprog 
Requires:         R-methods 
Requires:         R-stats 

%description
Implements Lagrangian multiplier smoothing splines for flexible
nonparametric regression and function estimation. Provides tools for
fitting, prediction, and inference using a constrained optimization
approach to enforce smoothness. Supports generalized linear models,
Weibull accelerated failure time (AFT) models, quadratic programming
constraints, and customizable working-correlation structures, with options
for parallel fitting. The core spline construction builds on Ezhov et al.
(2018) <doi:10.1515/jag-2017-0029>. Quadratic-programming and SQP details
follow Goldfarb & Idnani (1983) <doi:10.1007/BF02591962> and Nocedal &
Wright (2006) <doi:10.1007/978-0-387-40065-5>. For smoothing spline and
penalized spline background, see Wahba (1990)
<doi:10.1137/1.9781611970128> and Wood (2017) <doi:10.1201/9781315370279>.
For variance-component and correlation-parameter estimation, see Searle et
al. (2006) <ISBN:978-0470009598>. The default multivariate partitioning
step uses k-means clustering as in MacQueen (1967).

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
