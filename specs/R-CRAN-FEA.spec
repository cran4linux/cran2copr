%global __brp_check_rpaths %{nil}
%global packname  FEA
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Finite Element Modeling for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ptinpoly 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ptinpoly 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-MASS 

%description
Finite element modeling of 2D geometries using constant strain triangles.
Applies material properties and boundary conditions (load and constraint)
to generate a finite element model. The model produces stress, strain, and
nodal displacements; a heat map is available to demonstrate regions where
output variables are high or low.  Also provides options for creating a
triangular mesh of 2D geometries. Package developed with reference to:
Bathe, K. J. (1996). Finite Element Procedures.[ISBN 978-0-9790049-5-7] --
Seshu, P. (2012). Textbook of Finite Element Analysis.
[ISBN-978-81-203-2315-5] -- Mustapha, K. B. (2018). Finite Element
Computations in Mechanics with R. [ISBN 9781315144474].

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
