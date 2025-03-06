%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  habtools
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools and Metrics for 3D Surfaces and Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.5
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-raster >= 3.5
Requires:         R-CRAN-terra 
Requires:         R-methods 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-dplyr 

%description
A collection of functions for sampling and simulating 3D surfaces and
objects and estimating metrics like rugosity, fractal dimension,
convexity, sphericity, circularity, second moments of area and volume, and
more.

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
