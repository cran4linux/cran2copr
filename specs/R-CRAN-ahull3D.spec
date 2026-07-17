%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ahull3D
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast 3D Alpha Hull with Label Propagation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-Rvcg >= 0.18
BuildRequires:    R-CRAN-rgl >= 0.100.0
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppCGAL 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-Rvcg >= 0.18
Requires:         R-CRAN-rgl >= 0.100.0

%description
Fast 3D alpha shape (alpha hull) computation with label propagation from
input points to hull vertices and faces. Uses 'CGAL' for robust geometric
computations. Optimized for Light Detection and Ranging ('LiDAR')
processing and tree segmentation workflows. The implementation follows the
alpha shape algorithm described in Edelsbrunner et al. (1983)
<doi:10.1007/BF02579193>.

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
