%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  centerline
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Centerline from Closed Polygons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-wk >= 0.9
BuildRequires:    R-CRAN-sfnetworks >= 0.6
BuildRequires:    R-CRAN-geos >= 0.2.4
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-wk >= 0.9
Requires:         R-CRAN-sfnetworks >= 0.6
Requires:         R-CRAN-geos >= 0.2.4
Requires:         R-CRAN-checkmate 

%description
Generates skeletons of closed 2D polygons using Voronoi diagrams. It
provides methods for 'sf', 'terra', and 'geos' objects to compute polygon
centerlines based on the generated skeletons. Voronoi, G. (1908)
<doi:10.1515/crll.1908.134.198>.

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
