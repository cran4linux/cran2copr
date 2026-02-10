%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BCSreg
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Box-Cox Symmetric Regression for Non-Negative Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-GeneralizedHyperbolic 

%description
A collection of tools for regression analysis of non-negative data,
including strictly positive and zero-inflated observations, based on the
class of the Box-Cox symmetric (BCS) distributions and its zero-adjusted
extension. The BCS distributions are a class of flexible probability
models capable of describing different levels of skewness and
tail-heaviness. The package offers a comprehensive regression modeling
framework, including estimation and tools for evaluating goodness-of-fit.

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
