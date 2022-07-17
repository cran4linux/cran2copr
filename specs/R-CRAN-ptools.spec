%global __brp_check_rpaths %{nil}
%global packname  ptools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Poisson Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-stats 
Requires:         R-methods 

%description
Functions used for analyzing count data, mostly crime counts. Includes
checking difference in two Poisson counts (e-test), checking the fit for a
Poisson distribution, small sample tests for counts in bins (Wheeler,
????) <doi:10.1002/jip.1449>, Weighted Displacement Difference test
(Wheeler and Ratcliffe, 2018) <doi:10.1186/s40163-018-0085-5>, to evaluate
crime changes over time in treated/control areas. Additionally includes
functions for aggregating spatial data and spatial feature engineering.

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
