%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aws.wrfsmn
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Data Processing of SMN Hi-Res Weather Forecast from 'AWS'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.1.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-lubridate >= 1.9.3
BuildRequires:    R-CRAN-terra >= 1.7.65
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-hydroGOF >= 0.5.4
BuildRequires:    R-CRAN-aws.s3 >= 0.3.21
Requires:         R-stats >= 4.1.2
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-lubridate >= 1.9.3
Requires:         R-CRAN-terra >= 1.7.65
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-hydroGOF >= 0.5.4
Requires:         R-CRAN-aws.s3 >= 0.3.21

%description
Exploration of Weather Research & Forecasting ('WRF') Model data of
Servicio Meteorologico Nacional (SMN) from Amazon Web Services
(<https://registry.opendata.aws/smn-ar-wrf-dataset/>) cloud. The package
provides the possibility of data downloading, processing and correction
methods. It also has map management and series exploration of available
meteorological variables of 'WRF' forecast.

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
