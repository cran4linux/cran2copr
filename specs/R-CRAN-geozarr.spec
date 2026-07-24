%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geozarr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          GeoZarr Conventions for Geospatial Data in Zarr Stores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-CFtime >= 1.7.3
BuildRequires:    R-CRAN-zarr >= 0.4.2
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-CFtime >= 1.7.3
Requires:         R-CRAN-zarr >= 0.4.2
Requires:         R-CRAN-R6 

%description
Large-scale gridded data stores are increasingly using the Zarr format.
GeoZarr is defined in terms of a number of community conventions built on
top of the Zarr specification. These conventions specify how Zarr metadata
is to be interpreted to attach semantic meaning to the data in the Zarr
array providing the metadata. This package implements a number of
community conventions on top of the 'zarr' package, enabling the R
community to use geospatial data stored in Zarr.

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
