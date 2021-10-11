%global __brp_check_rpaths %{nil}
%global packname  rayvertex
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          3D Software Rasterizer

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rayimage 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-spacefillr 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-magrittr 
Requires:         R-grDevices 
Requires:         R-CRAN-rayimage 
Requires:         R-CRAN-png 
Requires:         R-CRAN-digest 

%description
Rasterize images using a 3D software renderer. 3D scenes are created
either by importing external files, building scenes out of the included
objects, or by constructing meshes manually. Supports point and
directional lights, anti-aliased lines, shadow mapping, transparent
objects, translucent objects, multiple materials types, reflection,
refraction, environment maps, multicore rendering, bloom, tone-mapping,
and screen-space ambient occlusion.

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
