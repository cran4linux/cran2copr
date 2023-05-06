%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastclime
%global packver   1.4.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Fast Solver for Parameterized LP Problems, Constrained L1 Minimization Approach to Sparse Precision Matrix Estimation and Dantzig Selector

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Provides a method of recovering the precision matrix efficiently and
solving for the dantzig selector by applying the parametric simplex
method.  The computation is based on a linear optimization solver. It also
contains a generic LP solver and a parameterized LP solver using
parametric simplex method.

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
