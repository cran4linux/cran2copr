%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ip2locationio
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lookup Geolocation and Proxy Information using 'IP2Location.io' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-reticulate >= 1.13
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-reticulate >= 1.13

%description
Query for enriched data such as country, region, city, latitude &
longitude, ZIP code, time zone, Autonomous System, Internet Service
Provider, domain, net speed, International direct dialing (IDD) code, area
code, weather station data, mobile data, elevation, usage type, address
type, advertisement category, fraud score, and proxy data with an IP
address. You can also query a list of hosted domain names for the IP
address too. This package uses the 'IP2Location.io' API to query this
data. To get started with a free API key, sign up here
<https://www.ip2location.io/sign-up?ref=1>.

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
