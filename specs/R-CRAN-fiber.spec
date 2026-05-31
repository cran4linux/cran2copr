%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fiber
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          S7 Data Structures for Diffusion MRI Tractography

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-S7 

%description
Provides three S7 classes — streamline, bundle, and bundle_set — for
representing diffusion MRI tractography data in R, together with a concise
set of methods for computing shape descriptors (arc-length, curvature,
torsion, sinuosity), the Hausdorff distance between streamlines,
arc-length reparametrization of streamlines and bundles onto uniform
grids, combination of streamlines or bundles into a single bundle,
combination of bundles from multiple subjects or sessions into a
bundle_set, and coercion to and from the dwiFiber S4 class of the 'dti'
package. See Dell'Acqua, F., Descoteaux, M. and Leemans, A. (2024)
"Handbook of Diffusion MR Tractography" <doi:10.1016/C2018-0-02520-7> for
more about the mathematical and computational underpinnings of diffusion
MRI tractography.

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
