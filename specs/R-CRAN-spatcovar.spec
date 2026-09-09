%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatcovar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Spatial Covariates from Polygon Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-exactextractr >= 0.9.0
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-exactextractr >= 0.9.0
Requires:         R-CRAN-terra 
Requires:         R-CRAN-units 

%description
Provides a consistent interface for constructing commonly used spatial
covariates from polygon data. Computes polygon areas, distances to
reference features, point and line intersection counts, line lengths
within polygons, polygon overlap areas and shares, and raster zonal
summaries. Handles coordinate reference system validation, geometry
repair, unit conversion, row preservation, and standardised missing value
semantics while relying on established spatial libraries for the
underlying geometry operations.

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
