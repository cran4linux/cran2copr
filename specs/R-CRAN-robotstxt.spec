%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robotstxt
%global packver   0.7.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.15
Release:          1%{?dist}%{?buildtag}
Summary:          A 'robots.txt' Parser and 'Webbot'/'Spider'/'Crawler' Permissions Checker

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-future.apply >= 1.0.0
BuildRequires:    R-CRAN-spiderbar >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-future.apply >= 1.0.0
Requires:         R-CRAN-spiderbar >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Provides functions to download and parse 'robots.txt' files. Ultimately
the package makes it easy to check if bots (spiders, crawler, scrapers,
...) are allowed to access specific resources on a domain.

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
