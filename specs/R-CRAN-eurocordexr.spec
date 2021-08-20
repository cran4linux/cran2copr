%global __brp_check_rpaths %{nil}
%global packname  eurocordexr
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Makes it Easier to Work with Daily 'netCDF' from EURO-CORDEX RCMs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-ncdf4.helpers 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-ncdf4.helpers 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-PCICt 
Requires:         R-CRAN-lubridate 

%description
Daily 'netCDF' data from e.g. regional climate models (RCMs) are not
trivial to work with. This package, which relies on 'data.table', makes it
easier to deal with large data from RCMs, such as from EURO-CORDEX
(<https://www.euro-cordex.net/>, <https://cordex.org/data-access/>). It
has functions to extract single grid cells from rotated pole grids as well
as the whole array in long format. Can handle non-standard calendars (360,
noleap) and interpolate them to a standard one. Potentially works with
many CF-conform 'netCDF' files.

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
