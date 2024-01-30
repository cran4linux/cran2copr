%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tetrascatt
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Acoustic Scattering for Complex Shapes by Using the DWBA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9

%description
Uses the Distorted Wave Born Approximation (DWBA) to compute the acoustic
backward scattering, the geometry of the object is formed by a volumetric
mesh, composed of tetrahedrons. This computation is done efficiently
through an analytical 3D integration that allows for a solution which is
expressed in terms of elementary functions for each tetrahedron. It is
important to note that this method is only valid for objects whose
acoustic properties, such as density and sound speed, do not vary
significantly compared to the surrounding medium. (See Lavia, Cascallares
and Gonzalez, J. D. (2023). TetraScatt model: Born approximation for the
estimation of acoustic dispersion of fluid-like objects of arbitrary
geometries. arXiv preprint <arXiv:2312.16721>).

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
