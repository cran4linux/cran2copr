%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeoThinneR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Spatial Thinning of Species Occurrences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Provides efficient geospatial thinning algorithms to reduce the density of
coordinate data while maintaining spatial relationships. Implements K-D
Tree and brute-force distance-based thinning, as well as grid-based and
precision-based thinning methods. For more information on the methods, see
Elseberg et al. (2012) <https://hdl.handle.net/10446/86202>.

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
