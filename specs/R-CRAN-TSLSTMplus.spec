%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSLSTMplus
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Long-Short Term Memory for Time-Series Forecasting, Enhanced

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-tsutils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-tsutils 
Requires:         R-stats 
Requires:         R-CRAN-abind 

%description
The LSTM (Long Short-Term Memory) model is a Recurrent Neural Network
(RNN) based architecture that is widely used for time series forecasting.
Customizable configurations for the model are allowed, improving the
capabilities and usability of this model compared to other packages. This
package is based on 'keras' and 'tensorflow' modules and the algorithm of
Paul and Garai (2021) <doi:10.1007/s00500-021-06087-4>.

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
