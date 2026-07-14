%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hcinfer
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Heteroskedasticity-Consistent Inference for Linear Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Computes heteroskedasticity-consistent covariance matrix estimators for
ordinary least squares regression models. The published HC0 through HC5m
estimators implemented in the package follow White (1980)
<doi:10.2307/1912934>, Hinkley (1977)
<doi:10.1080/00401706.1977.10489550>, Horn et al. (1975)
<doi:10.1080/01621459.1975.10479877>, MacKinnon and White (1985)
<doi:10.1016/0304-4076(85)90158-7>, Cribari-Neto (2004)
<doi:10.1016/S0167-9473(02)00366-3>, Cribari-Neto and da Silva (2011)
<doi:10.1007/s10182-010-0141-2>, Cribari-Neto et al. (2007)
<doi:10.1080/03610920601126589>, and Li et al. (2016)
<doi:10.1080/00949655.2016.1198906>. The package also includes HCbeta, a
new estimator proposed by the package authors. It provides normal Wald
tests, confidence intervals, diagnostics, and S3 output for applied
inference.

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
