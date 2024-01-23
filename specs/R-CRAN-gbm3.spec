%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbm3
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Boosted Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-splines 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-lattice 
Requires:         R-splines 

%description
Extensions to Freund and Schapire's AdaBoost algorithm, Y. Freund and R.
Schapire (1997) <doi:10.1006/jcss.1997.1504> and Friedman's gradient
boosting machine, J.H. Friedman (2001) <doi:10.1214/aos/1013203451>.
Includes regression methods for least squares, absolute loss,
t-distribution loss, quantile regression, logistic, Poisson, Cox
proportional hazards partial likelihood, AdaBoost exponential loss,
Huberized hinge loss, and Learning to Rank measures (LambdaMART).

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
