%global __brp_check_rpaths %{nil}
%global packname  smooth
%global packver   3.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting Using State Space Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-greybox >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.100.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-greybox >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nloptr 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Functions implementing Single Source of Error state space models for
purposes of time series analysis and forecasting. The package includes
ADAM (Svetunkov, 2021, <https://openforecast.org/adam/>), Exponential
Smoothing (Hyndman et al., 2008, <doi: 10.1007/978-3-540-71918-2>), SARIMA
(Svetunkov & Boylan, 2019 <doi: 10.1080/00207543.2019.1600764>), Complex
Exponential Smoothing (Svetunkov & Kourentzes, 2018, <doi:
10.13140/RG.2.2.24986.29123>), Simple Moving Average (Svetunkov &
Petropoulos, 2018 <doi: 10.1080/00207543.2017.1380326>) and several
simulation functions. It also allows dealing with intermittent demand
based on the iETS framework (Svetunkov & Boylan, 2019, <doi:
10.13140/RG.2.2.35897.06242>).

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
