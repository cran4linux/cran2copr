%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gdistance
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Distances and Routes on Geographical Grids

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 1.9.19
BuildRequires:    R-CRAN-igraph >= 0.7.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-raster >= 1.9.19
Requires:         R-CRAN-igraph >= 0.7.0
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Provides classes and functions to calculate various distance measures and
routes in heterogeneous geographic spaces represented as grids. The
package implements measures to model dispersal histories first presented
by van Etten and Hijmans (2010) <doi:10.1371/journal.pone.0012060>.
Least-cost distances as well as more complex distances based on
(constrained) random walks can be calculated. The distances implemented in
the package are used in geographical genetics, accessibility indicators,
and may also have applications in other fields of geospatial analysis.

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
