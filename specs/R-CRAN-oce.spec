%global packname  oce
%global packver   1.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Oceanographic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-gsw 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-gsw 
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Supports the analysis of Oceanographic data, including 'ADCP'
measurements, measurements made with 'argo' floats, 'CTD' measurements,
sectional data, sea-level time series, coastline and topographic data,
etc. Provides specialized functions for calculating seawater properties
such as potential temperature in either the 'UNESCO' or 'TEOS-10' equation
of state. Produces graphical displays that conform to the conventions of
the Oceanographic literature. This package is discussed extensively in Dan
Kelley's book Oceanographic Analysis with R, published in 2018 by
'Springer-Verlag' with ISBN 978-1-4939-8842-6.

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
