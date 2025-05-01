%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RNetCDF
%global packver   2.11-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'NetCDF' Datasets

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    netcdf-devel
BuildRequires:    udunits2-devel
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
An interface to the 'NetCDF' file formats designed by Unidata for
efficient storage of array-oriented scientific data and descriptions. Most
capabilities of 'NetCDF' version 4 are supported. Optional conversions of
time units are enabled by 'UDUNITS' version 2, also from Unidata.

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
