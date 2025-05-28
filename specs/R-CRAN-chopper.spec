%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chopper
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Changepoint-Aware Ensemble for Probabilistic Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.21
BuildRequires:    R-CRAN-fGarch >= 4022
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-imputeTS >= 3.3
BuildRequires:    R-CRAN-evd >= 2.3.6.1
BuildRequires:    R-CRAN-changepoint >= 2.3
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-ald >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-GeneralizedHyperbolic >= 0.8.6
BuildRequires:    R-CRAN-normalp >= 0.7.2
Requires:         R-CRAN-forecast >= 8.21
Requires:         R-CRAN-fGarch >= 4022
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-imputeTS >= 3.3
Requires:         R-CRAN-evd >= 2.3.6.1
Requires:         R-CRAN-changepoint >= 2.3
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-ald >= 1.3.1
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-GeneralizedHyperbolic >= 0.8.6
Requires:         R-CRAN-normalp >= 0.7.2

%description
Implements a changepoint-aware ensemble forecasting algorithm that
combines Theta, TBATS (Trigonometric, Box-Cox transformation, ARMA errors,
Trend, Seasonal components), and ARFIMA (AutoRegressive, Fractionally
Integrated, Moving Average) using a product-of-experts approach for robust
probabilistic prediction.

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
