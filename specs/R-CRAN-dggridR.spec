%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dggridR
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Global Grids

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods >= 3.4.0
BuildRequires:    R-CRAN-sp >= 1.2
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.4
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods >= 3.4.0
Requires:         R-CRAN-sp >= 1.2
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-dplyr >= 0.4
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-Rcpp >= 0.12.12

%description
Spatial analyses involving binning require that every bin have the same
area, but this is impossible using a rectangular grid laid over the Earth
or over any projection of the Earth. Discrete global grids use hexagons,
triangles, and diamonds to overcome this issue, overlaying the Earth with
equally-sized bins. This package provides utilities for working with
discrete global grids, along with utilities to aid in plotting such data.

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
