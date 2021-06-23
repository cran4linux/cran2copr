%global __brp_check_rpaths %{nil}
%global packname  vcr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Record 'HTTP' Calls to Disk

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-crul >= 0.8.4
BuildRequires:    R-CRAN-webmockr >= 0.8.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-crul >= 0.8.4
Requires:         R-CRAN-webmockr >= 0.8.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-rprojroot 

%description
Record test suite 'HTTP' requests and replays them during future runs. A
port of the Ruby gem of the same name (<https://github.com/vcr/vcr/>).
Works by hooking into the 'webmockr' R package for matching 'HTTP'
requests by various rules ('HTTP' method, 'URL', query parameters,
headers, body, etc.), and then caching real 'HTTP' responses on disk in
'cassettes'. Subsequent 'HTTP' requests matching any previous requests in
the same 'cassette' use a cached 'HTTP' response.

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
