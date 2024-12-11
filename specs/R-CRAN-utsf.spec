%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  utsf
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate Time Series Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-vctsfr 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ipred 
Requires:         R-methods 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-vctsfr 

%description
An engine for univariate time series forecasting using different
regression models in an autoregressive way. The engine provides an uniform
interface for applying the different models. Furthermore, it is extensible
so that users can easily apply their own regression models to univariate
time series forecasting and benefit from all the features of the engine,
such as preprocessings or estimation of forecast accuracy.

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
