%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbm
%global packver   2.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Boosted Regression Models

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-lattice 
Requires:         R-parallel 
Requires:         R-CRAN-survival 

%description
An implementation of extensions to Freund and Schapire's AdaBoost
algorithm and Friedman's gradient boosting machine. Includes regression
methods for least squares, absolute loss, t-distribution loss, quantile
regression, logistic, multinomial logistic, Poisson, Cox proportional
hazards partial likelihood, AdaBoost exponential loss, Huberized hinge
loss, and Learning to Rank measures (LambdaMart). Originally developed by
Greg Ridgeway. Newer version available at github.com/gbm-developers/gbm3.

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
