%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ModalForecast
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Modal ARIMA and Seasonal ARIMA Models using the SKD Family

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-grid 

%description
Implements parametric modal Autoregressive Integrated Moving Average
(ARIMA) and seasonal ARIMA (SARIMA) models utilizing the Skewed
Distribution (SKD) family, in which the conditional mode, rather than the
conditional mean, follows the (seasonal) ARIMA recursion. Current
distributions supported are the Skew-Normal, Skewed Student-t, and Skewed
Laplace. The parameters are estimated by maximum likelihood using
analytical gradients. Includes residual diagnostics, simulation envelopes,
automatic order selection, joint and marginal modal forecasts, exact and
parametric bootstrap prediction intervals, and classical asymptotic
inference via the Fisher Information matrix. Methods are described in
Galarza, C.E., Lachos, V.H., Cabral, C.R.B., & Castro, L.M. (2017)
<doi:10.1002/sta4.140>.

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
