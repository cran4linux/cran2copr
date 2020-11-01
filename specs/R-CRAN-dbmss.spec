%global packname  dbmss
%global packver   2.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Distance-Based Measures of Spatial Structures

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-CRAN-tibble 

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
