%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcount
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Marginalized Count Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-boot.pval 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-boot.pval 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Implementation of marginalized models for zero-inflated count data. The
package provides tools to estimate marginalized count regression models
for direct inference on the effect of covariates on the marginal mean of
the outcome. The methods include the marginalized zero-inflated Poisson
(MZIP) model described in Long et al. (2014) <doi:10.1002/sim.6293> and
the marginalized zero- and N-inflated binomial (MZNIB) model, which
extends marginalized modeling to fractional count outcomes with boundary
inflation at zero and the upper limit.

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
