%global __brp_check_rpaths %{nil}
%global packname  movecost
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of Slope-Dependant Accumulated Cost Surface, Least-Cost Paths, Least-Cost Corridors, Least-Cost Networks Related to Human Movement Across the Landscape

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.0.3
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-CRAN-raster >= 2.8.4
BuildRequires:    R-CRAN-chron >= 2.3.56
BuildRequires:    R-CRAN-spatstat.geom >= 2.2.0
BuildRequires:    R-CRAN-rgdal >= 1.5.0
BuildRequires:    R-CRAN-sp >= 1.4.0
BuildRequires:    R-CRAN-gdistance >= 1.2.2
BuildRequires:    R-CRAN-maptools >= 1.1.0
BuildRequires:    R-CRAN-rgeos >= 0.4.2
BuildRequires:    R-CRAN-elevatr >= 0.3.4
Requires:         R-methods >= 4.0.3
Requires:         R-utils >= 4.0.0
Requires:         R-CRAN-raster >= 2.8.4
Requires:         R-CRAN-chron >= 2.3.56
Requires:         R-CRAN-spatstat.geom >= 2.2.0
Requires:         R-CRAN-rgdal >= 1.5.0
Requires:         R-CRAN-sp >= 1.4.0
Requires:         R-CRAN-gdistance >= 1.2.2
Requires:         R-CRAN-maptools >= 1.1.0
Requires:         R-CRAN-rgeos >= 0.4.2
Requires:         R-CRAN-elevatr >= 0.3.4

%description
Provides the facility to calculate non-isotropic accumulated cost surface,
least-cost paths, least-cost corridors, least-cost networks using a number
of human-movement-related cost functions that can be selected by the user.
It just requires a Digital Terrain Model, a start location and
(optionally) destination locations. See Alberti (2019)
<doi:10.1016/j.softx.2019.100331>.

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
