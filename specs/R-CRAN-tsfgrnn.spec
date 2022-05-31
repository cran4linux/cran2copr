%global __brp_check_rpaths %{nil}
%global packname  tsfgrnn
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Forecasting Using GRNN

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 

%description
A general regression neural network (GRNN) is a variant of a Radial Basis
Function Network characterized by a fast single-pass learning. 'tsfgrnn'
allows you to forecast time series using a GRNN model Francisco Martinez
et al. (2019) <doi:10.1007/978-3-030-20521-8_17> and Francisco Martinez et
al. (2022) <doi:10.1016/j.neucom.2021.12.028>. When the forecasting
horizon is higher than 1, two multi-step ahead forecasting strategies can
be used. The model built is autoregressive, that is, it is only based on
the observations of the time series. You can consult and plot how the
prediction was done. It is also possible to assess the forecasting
accuracy of the model using rolling origin evaluation.

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
