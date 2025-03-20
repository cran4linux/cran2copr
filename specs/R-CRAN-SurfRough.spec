%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurfRough
%global packver   0.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Surface/Image Texture Indexes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-terra 

%description
Methods for the computation of surface/image texture indices using a
geostatistical based approach (Trevisani et al. (2023)
<doi:10.1016/j.geomorph.2023.108838>). It provides various functions for
the computation of surface texture indices (e.g., omnidirectional
roughness and roughness anisotropy), including the ones based on the
robust MAD estimator. The kernels included in the software permit also to
calculate the surface/image texture indices directly from the input
surface (i.e., without de-trending) using increments of order 2. It also
provides the new radial roughness index (RRI), representing the
improvement of the popular topographic roughness index (TRI). The
framework can be easily extended with ad-hoc surface/image texture
indices.

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
