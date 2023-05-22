%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbmss
%global packver   2.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Distance-Based Measures of Spatial Structures

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 

%description
Simple computation of spatial statistic functions of distance to
characterize the spatial structures of mapped objects, following Marcon,
Traissac, Puech, and Lang (2015) <doi:10.18637/jss.v067.c03>. Includes
classical functions (Ripley's K and others) and more recent ones used by
spatial economists (Duranton and Overman's Kd, Marcon and Puech's M).
Relies on 'spatstat' for some core calculation.

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
