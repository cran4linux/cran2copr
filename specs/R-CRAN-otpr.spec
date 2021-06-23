%global __brp_check_rpaths %{nil}
%global packname  otpr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          An R Wrapper for the 'OpenTripPlanner' REST API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rrapply 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rrapply 
Requires:         R-CRAN-rlang 

%description
A wrapper for the 'OpenTripPlanner' <http://www.opentripplanner.org/> REST
API. Queries are submitted to the relevant 'OpenTripPlanner' API resource,
the response is parsed and useful R objects are returned.

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
