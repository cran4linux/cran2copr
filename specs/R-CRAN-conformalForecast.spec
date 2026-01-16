%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conformalForecast
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conformal Prediction Methods for Multistep-Ahead Time Series Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
Methods and tools for performing multistep-ahead time series forecasting
using conformal prediction methods including classical conformal
prediction, adaptive conformal prediction, conformal PID
(Proportional-Integral-Derivative) control, and autocorrelated
multistep-ahead conformal prediction. The methods were described by Wang
and Hyndman (2024) <doi:10.48550/arXiv.2410.13115>.

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
