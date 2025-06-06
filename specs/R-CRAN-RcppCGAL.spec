%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppCGAL
%global packver   6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Rcpp' Integration for 'CGAL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Creates a header only package to link to the 'CGAL' (Computational
Geometry Algorithms Library) header files in 'Rcpp'. There are a variety
of potential uses for the software such as Hilbert sorting, K-D Tree
nearest neighbors, and convex hull algorithms. For more information about
how to use the header files, see the 'CGAL' documentation at
<https://www.cgal.org>. Currently downloads version 6.0.1 of the 'CGAL'
header files.

%prep
%setup -q -c -n %{packname}
tar xf %{SOURCE1} -C %{packname}/inst */include --strip-components=1
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
