%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMAWGEN
%global packver   1.3.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Site Auto-Regressive Weather GENerator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-date 
Requires:         R-CRAN-vars 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
S3 and S4 functions are implemented for spatial multi-site stochastic
generation of daily time series of temperature and precipitation. These
tools make use of Vector AutoRegressive models (VARs). The weather
generator model is then saved as an object and is calibrated by daily
instrumental "Gaussianized" time series through the 'vars' package tools.
Once obtained this model, it can it can be used for weather generations
and be adapted to work with several climatic monthly time series.

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
