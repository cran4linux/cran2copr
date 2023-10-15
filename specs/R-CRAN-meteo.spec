%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  meteo
%global packver   2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          RFSI and Spatio-Temporal Geostatistical Interpolation for Meteorological and Other Environmental Variables

License:          GPL (>= 2.0) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-CAST 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sftime 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-terra 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-units 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-CAST 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sftime 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-terra 

%description
RFSI and spatio-temporal geostatistical interpolation for meteorological
and other environmental variables. Global spatio-temporal models
calculated using publicly available data are stored in package.

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
