%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evapoRe
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evapotranspiration R Recipes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-twc 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-twc 

%description
An R-based application for exploratory data analysis of global
EvapoTranspiration (ET) datasets. 'evapoRe' enables users to download,
validate, visualize, and analyze multi-source ET data across various
spatio-temporal scales. Also, the package offers calculation methods for
estimating potential ET (PET), including temperature-based, combined type,
and radiation-based approaches described in : Oudin et al., (2005)
<doi:10.1016/j.jhydrol.2004.08.026>. 'evapoRe' supports hydrological
modeling, climate studies, agricultural research, and other data-driven
fields by facilitating access to ET data and offering powerful analysis
capabilities. Users can seamlessly integrate the package into their
research applications and explore diverse ET data at different
resolutions.

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
