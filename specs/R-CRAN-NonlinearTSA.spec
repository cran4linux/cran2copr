%global __brp_check_rpaths %{nil}
%global packname  NonlinearTSA
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-tsDyn 
BuildRequires:    R-CRAN-minpack.lm 
Requires:         R-CRAN-car 
Requires:         R-CRAN-tsDyn 
Requires:         R-CRAN-minpack.lm 

%description
Function and data sets in the book entitled "Nonlinear Time Series
Analysis with R Applications" B.Guris (2020). The book will be published
in Turkish and the original name of this book will be "R Uygulamali
Dogrusal Olmayan Zaman Serileri Analizi". It is possible to perform
nonlinearity tests, nonlinear unit root tests, nonlinear cointegration
tests and estimate nonlinear error correction models by using the
functions written in this package. The Momentum Threshold Autoregressive
(MTAR), the Smooth Threshold Autoregressive (STAR) and the Self Exciting
Threshold Autoregressive (SETAR) type unit root tests can be performed
using the functions written. In addition, cointegration tests using the
Momentum Threshold Autoregressive (MTAR), the Smooth Threshold
Autoregressive (STAR) and the Self Exciting Threshold Autoregressive
(SETAR) models can be applied. It is possible to estimate nonlinear error
correction models. The Granger causality test performed using nonlinear
models can also be applied.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
