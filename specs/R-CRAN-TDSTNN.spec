%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDSTNN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Delay Spatio Temporal Neural Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.3
Requires:         R-core >= 4.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-nnet 

%description
STARMA (Space-Time Autoregressive Moving Average) models are commonly
utilized in modeling and forecasting spatiotemporal time series data.
However, the intricate nonlinear dynamics observed in many space-time
rainfall patterns often exceed the capabilities of conventional STARMA
models. This R package enables the fitting of Time Delay Spatio-Temporal
Neural Networks, which are adept at handling such complex nonlinear
dynamics efficiently. For detailed methodology, please refer to Saha et
al. (2020) <doi:10.1007/s00704-020-03374-2>.

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
