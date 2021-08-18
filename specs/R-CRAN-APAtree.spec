%global __brp_check_rpaths %{nil}
%global packname  APAtree
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of the 'Area Potentially Available' (APA) to Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-FD 
Requires:         R-parallel 
Requires:         R-CRAN-units 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 

%description
Maps of the 'area potentially available' (APA) of trees is calculated from
mapped forest stands using the approach from Gspaltl et al. (2012)
<doi:10.1093/forestry/cps052>. This is done by computing a rasterized
version of 'weighted voronoi diagrams' using a an approximation of the
trees competitive ability (e.g., crown radius, leaf area) as weight. The
main output are 'Raster*'- objects from the 'raster' package that are
stored together with the raw data in apa_list's, the main class of the
'APAtree' package. Aggregation functions are provided to calculate stand
characteristics based on APA-maps such as relative proportions according
to APA-size and the neighborhood diversity index NDiv (Glatthorn (2021)
<doi:10.1016/j.ecolind.2021.108073>).

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
