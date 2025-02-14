%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fracARMA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fractionally Integrated ARMA Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fracdiff 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fracdiff 

%description
Implements fractional differencing with Autoregressive Moving Average
models to analyse long-memory time series data. Traditional ARIMA models
typically use integer values for differencing, which are suitable for time
series with short memory or anti-persistent behaviour. In contrast, the
Fractional ARIMA model allows fractional differencing, enabling it to
effectively capture long memory characteristics in time series data. The
‘fracARMA’ package is user-friendly and allows users to manually input the
fractional differencing parameter, which can be obtained using various
estimators such as the GPH estimator, Sperio method, or Wavelet method and
many. Additionally, the package enables users to directly feed the time
series data, AR order, MA order, fractional differencing parameter, and
the proportion of training data as a split ratio, all in a single command.
The package is based on the reference from the paper of Irshad and others
(2024, <doi:10.22271/maths.2024.v9.i6b.1906>).

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
