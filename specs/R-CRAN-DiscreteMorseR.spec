%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiscreteMorseR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Morse Theory for 3D Meshes Derived from Point Clouds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-gtools >= 3.8.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.18.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-furrr >= 0.2.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-gtools >= 3.8.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.0
Requires:         R-CRAN-future >= 1.18.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-furrr >= 0.2.0

%description
Ultra-fast computation of discrete Morse (Marston Morse) gradient vector
fields and critical simplices (0-simplices: vertices, 1-simplices: edges,
2-simplices: faces) on 3D triangular meshes from point clouds. Provides
C++ backend with parallel processing for large-scale topological analysis,
including connected component analysis and visualization tools. Perfect
for Light Detection and Ranging ('LiDAR') data, computational topology,
and geometric analysis applications. The implementation follows Forman
(1998) <doi:10.1007/PL00009307> for discrete Morse theory, with extensions
for 3D mesh processing.

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
