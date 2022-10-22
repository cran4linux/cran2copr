%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mgcv
%global packver   1.8-41
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.41
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed GAM Computation Vehicle with Automatic Smoothness Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-nlme >= 3.1.64
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
Requires:         R-CRAN-nlme >= 3.1.64
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 
Requires:         R-utils 

%description
Generalized additive (mixed) models, some of their extensions and other
generalized ridge regression with multiple smoothing parameter estimation
by (Restricted) Marginal Likelihood, Generalized Cross Validation and
similar, or using iterated nested Laplace approximation for fully Bayesian
inference. See Wood (2017) <doi:10.1201/9781315370279> for an overview.
Includes a gam() function, a wide variety of smoothers, 'JAGS' support and
distributions beyond the exponential family.

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
