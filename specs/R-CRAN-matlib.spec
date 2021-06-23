%global __brp_check_rpaths %{nil}
%global packname  matlib
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Matrix Functions for Teaching and Learning Linear Algebra and Multivariate Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-car 
Requires:         R-methods 

%description
A collection of matrix functions for teaching and learning matrix linear
algebra as used in multivariate statistical methods. These functions are
mainly for tutorial purposes in learning matrix algebra ideas using R. In
some cases, functions are provided for concepts available elsewhere in R,
but where the function call or name is not obvious. In other cases,
functions are provided to show or demonstrate an algorithm. In addition, a
collection of functions are provided for drawing vector diagrams in 2D and
3D.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
