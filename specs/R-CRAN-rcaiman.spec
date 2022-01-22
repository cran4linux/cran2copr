%global __brp_check_rpaths %{nil}
%global packname  rcaiman
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for CAnopy IMage ANalysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-spatial 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-spatial 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-rgdal 

%description
Its main strength is to classify hemispherical photographs of the plant
canopy with algorithms specially developed for such a task and well
documented in Díaz and Lencinas (2015) <doi:10.1109/lgrs.2015.2425931> and
Díaz and Lencinas (2018) <doi:10.1139/cjfr-2018-0006>. It supports
non-circular hemispherical photography.

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
