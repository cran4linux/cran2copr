%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rechaRge
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          HydroBudget – Groundwater Recharge Model

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-airGR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-hydrostats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-airGR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-hydrostats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-R.utils 

%description
HydroBudget is a spatially distributed groundwater recharge model that
computes a superficial water budget on grid cells with outputs aggregated
into monthly time steps. It was developed as an accessible and
computationally affordable model to simulate groundwater recharge over
large areas (thousands of km2, regional-scale watersheds) and for long
time periods (decades), in cold and humid climates. Model algorithms are
based on the research of Dubois, E. et al. (2021a)
<doi:10.5683/SP3/EUDV3H> and Dubois, E. et al. (2021b)
<doi:10.5194/hess-25-6567-2021>.

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
