%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aws.wrfsmn
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Processing of SMN Hi-Res Weather Forecast from 'AWS'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.65
BuildRequires:    R-CRAN-qpdf >= 1.3.2
BuildRequires:    R-CRAN-aws.s3 >= 0.3.21
Requires:         R-CRAN-terra >= 1.7.65
Requires:         R-CRAN-qpdf >= 1.3.2
Requires:         R-CRAN-aws.s3 >= 0.3.21

%description
Exploration of Weather Research & Forecasting ('WRF') Model data of
Servicio Meteorologico Nacional (SMN) from Amazon Web Services
(<https://registry.opendata.aws/smn-ar-wrf-dataset/>) cloud. The package
provides the possibility of data downloading and processing. It also has
map management and series exploration of available meteorological
variables of 'WRF' forecast.

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
