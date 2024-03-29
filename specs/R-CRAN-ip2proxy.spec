%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ip2proxy
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lookup for IP Address Proxy Information

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-maps >= 3.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-reticulate >= 1.13
Requires:         R-CRAN-maps >= 3.4.1
Requires:         R-CRAN-ggplot2 >= 3.4
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-reticulate >= 1.13

%description
Enable user to find the IP addresses which are used as VPN anonymizer,
open proxies, web proxies and Tor exits. The package lookup the proxy IP
address from IP2Proxy BIN Data file. You may visit
<https://lite.ip2location.com> for free database download.

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
