%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PlaneGeometry
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plane Geometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Carlson 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-fitConic 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-sdpt3r 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-uniformly 
Requires:         R-CRAN-Carlson 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-fitConic 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-sdpt3r 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-uniformly 

%description
An extensive set of plane geometry routines. Provides R6 classes
representing triangles, circles, circular arcs, ellipses, elliptical arcs,
lines, hyperbolae, and their plot methods. Also provides R6 classes
representing transformations: rotations, reflections, homotheties,
scalings, general affine transformations, inversions, Möbius
transformations.

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
