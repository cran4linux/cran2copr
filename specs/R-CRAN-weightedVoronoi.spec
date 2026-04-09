%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightedVoronoi
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Spatial Tessellations in Constrained Polygon Domains

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Matrix 

%description
Provides tools for weighted spatial tessellation using Euclidean and
geodesic distances within constrained polygonal domains. The package can
generate complete and connected spatial partitions that respect complex
boundaries, heterogeneous point weights, and optional resistance or
terrain effects. The methods extend weighted Voronoi tessellations to
constrained domains and graph-based cost-distance surfaces. For background
see Aurenhammer (1991) <doi:10.1145/116873.116880> and van Etten (2017)
<doi:10.18637/jss.v076.i13>.

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
