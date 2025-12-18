%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  osrm
%global packver   5.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface Between R and the OpenStreetMap-Based Routing Service OSRM

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mapiso 
BuildRequires:    R-CRAN-googlePolylines 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-curl 
Requires:         R-utils 
Requires:         R-CRAN-mapiso 
Requires:         R-CRAN-googlePolylines 
Requires:         R-CRAN-sf 

%description
An interface between R and the 'OSRM' API. 'OSRM' is a routing service
based on 'OpenStreetMap' data. See <http://project-osrm.org/> for more
information. This package enables the computation of routes, trips,
isochrones and travel distances matrices (travel time and kilometric
distance).

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
