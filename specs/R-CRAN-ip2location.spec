%global packname  ip2location
%global packver   8.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lookup for IP Address Information

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-reticulate >= 1.13
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-reticulate >= 1.13

%description
Enables the user to find the country, region, city, coordinates, zip code,
time zone, ISP, domain name, connection type, area code, weather station
code, weather station name, mobile, usage type, address type and IAB
category that any IP address or hostname originates from. Supported IPv4
and IPv6. Please visit <https://www.ip2location.com> to learn more. You
may also want to visit <https://lite.ip2location.com> for free database
download. This package requires 'IP2Location Python' module. At the
terminal, please run 'pip install IP2Location' to install the module.

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
