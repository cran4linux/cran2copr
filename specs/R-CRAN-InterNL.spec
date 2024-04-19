%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  InterNL
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Intervention Model Using Non-Linear Function

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-MLmetrics 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-MLmetrics 

%description
Intervention analysis is used to investigate structural changes in data
resulting from external events. Traditional time series intervention
models, viz. Autoregressive Integrated Moving Average model with
exogeneous variables (ARIMA-X) and Artificial Neural Networks with
exogeneous variables (ANN-X), rely on linear intervention functions such
as step or ramp functions, or their combinations. In this package, the
Gompertz, Logistic, Monomolecular, Richard and Hoerl function have been
used as non-linear intervention function. The equation of the above models
are represented as: Gompertz: A * exp(-B * exp(-k * t)); Logistic: K / (1
+ ((K - N0) / N0) * exp(-r * t)); Monomolecular: A * exp(-k * t); Richard:
A + (K - A) / (1 + exp(-B * (C - t)))^(1/beta) and Hoerl:
a*(b^t)*(t^c).This package introduced algorithm for time series
intervention analysis employing ARIMA and ANN models with a non-linear
intervention function. This package has been developed using algorithm of
Yeasin et al. <doi:10.1016/j.hazadv.2023.100325> and Paul and Yeasin
<doi:10.1371/journal.pone.0272999>.

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
