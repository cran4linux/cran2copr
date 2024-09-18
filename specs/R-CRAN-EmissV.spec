%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EmissV
%global packver   0.665.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.665.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Create Emissions for Air Quality Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-units >= 0.5.1
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-units >= 0.5.1
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
Processing tools to create emissions for use in numerical air quality
models. Emissions can be calculated both using emission factors and
activity data (Schuch et al 2018) <doi:10.21105/joss.00662> or using
pollutant inventories (Schuch et al., 2018) <doi:10.30564/jasr.v1i1.347>.
Functions to process individual point emissions, line emissions and area
emissions of pollutants are available as well as methods to incorporate
alternative data for Spatial distribution of emissions such as satellite
images (Gavidia-Calderon et. al, 2018)
<doi:10.1016/j.atmosenv.2018.09.026> or openstreetmap data (Andrade et al,
2015) <doi:10.3389/fenvs.2015.00009>.

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
