%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refundBayes
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Regression with Functional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.29.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.29.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-brms 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-splines2 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Bayesian regression with functional data, including regression with
scalar, survival, or functional outcomes. The package allows regression
with scalar and functional predictors. Methods are described in Jiang et
al. (2025) "Tutorial on Bayesian Functional Regression Using Stan"
<doi:10.1002/sim.70265>.

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
