%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ragg
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graphic Devices Based on AGG

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    freetype-devel
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    libpng-devel
BuildRequires:    libtiff-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-systemfonts >= 1.0.3
BuildRequires:    R-CRAN-textshaping >= 0.3.0
Requires:         R-CRAN-systemfonts >= 1.0.3
Requires:         R-CRAN-textshaping >= 0.3.0

%description
Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D
drawing library. The 'ragg' package provides a set of graphic devices
based on AGG to use as alternative to the raster devices provided through
the 'grDevices' package.

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
