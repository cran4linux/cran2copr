%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  potentiomap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build Potentiometric Surfaces and Flow Arrows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-fields 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Builds potentiometric surface products from groundwater monitoring data.
The package prepares groundwater observations from direct water-level
measurements or depth-to-water data paired with land-surface elevations,
interpolates thin-plate spline surfaces by default, supports alternative
and user-supplied interpolation methods, exports raster and contour
products, and derives hydraulic-gradient flow arrows. Raster operations
use methods from Hijmans (2025) <doi:10.32614/CRAN.package.terra>,
thin-plate spline interpolation uses methods from Nychka et al. (2021)
<doi:10.5065/D6W957CT>, and geostatistical interpolation uses methods from
Pebesma (2004) <doi:10.1016/j.cageo.2004.03.012>.

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
