%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geomattR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Geometric Attributes of Spatial Polygons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.8.70
BuildRequires:    R-CRAN-geosphere >= 1.5.20
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-terra >= 1.8.70
Requires:         R-CRAN-geosphere >= 1.5.20
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 

%description
Calculate geometric attributes of spatial polygons including area,
perimeter, compactness, elongation, orientation (bearing), fractal
dimension, and various shape indices. The package relies heavily on
'terra' methods and vector data objects
<https://github.com/rspatial/terra>.

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
