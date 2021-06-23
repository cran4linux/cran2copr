%global __brp_check_rpaths %{nil}
%global packname  bayesreg
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Regression Models with Global-Local Shrinkage Priors

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.0
BuildRequires:    R-CRAN-pgdraw >= 1.0
Requires:         R-stats >= 3.0
Requires:         R-CRAN-pgdraw >= 1.0

%description
Fits linear or generalized linear regression models using Bayesian
global-local shrinkage prior hierarchies as described in Polson and Scott
(2010) <doi:10.1093/acprof:oso/9780199694587.003.0017>. Provides an
efficient implementation of ridge, lasso, horseshoe and horseshoe+
regression with logistic, Gaussian, Laplace, Student-t, Poisson or
geometric distributed targets using the algorithms summarized in Makalic
and Schmidt (2016) <arXiv:1611.06649>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
