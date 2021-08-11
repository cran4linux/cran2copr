%global __brp_check_rpaths %{nil}
%global packname  CropScapeR
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access Cropland Data Layer Data via the 'CropScape' Web Service

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.6.1
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-RJSONIO >= 1.3
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-sf >= 0.8
Requires:         R-utils >= 3.6.1
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-RJSONIO >= 1.3
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-sf >= 0.8

%description
Interface to easily access Cropland Data Layer (CDL) data for any area of
interest via the 'CropScape' <https://nassgeodata.gmu.edu/CropScape/> web
service.

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
