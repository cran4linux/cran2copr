%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xaci
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Actuarial Climate Index

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-readr >= 2.1
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-ncdf4 >= 1.19
BuildRequires:    R-CRAN-dplyr >= 1.1
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-readr >= 2.1
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-ncdf4 >= 1.19
Requires:         R-CRAN-dplyr >= 1.1
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-units 
Requires:         R-parallel 

%description
Computes the Actuarial Climate Index (ACI) and its components
(temperature, precipitation, drought, wind, sea level) from gridded
climate data ('NetCDF') and tide gauge records. Implements the methodology
described in Garrido, Milhaud & Olympio (2025)
<https://hal.science/hal-04491982v2> for a French/European actuarial
climate index, building on the American Academy of Actuaries framework, to
any country in the world.

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
