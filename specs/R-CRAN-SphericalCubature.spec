%global __brp_check_rpaths %{nil}
%global packname  SphericalCubature
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Integration over Spheres and Balls in n-Dimensions; Multivariate Polar Coordinates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SimplicialCubature >= 1.3
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mvmesh 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-SimplicialCubature >= 1.3
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mvmesh 
Requires:         R-CRAN-abind 

%description
Provides several methods to integrate functions over the unit sphere and
ball in n-dimensional Euclidean space.  Routines for converting to/from
multivariate polar/spherical coordinates are also provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
