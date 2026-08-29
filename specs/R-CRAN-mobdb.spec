%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mobdb
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access the 'Mobility Database' API to Discover Transit Feeds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-digest 

%description
Search and access transit feed data from the 'Mobility Database'
<https://mobilitydatabase.org>. The package wraps the 'Mobility Database'
API, allowing users to discover 'GTFS' (General Transit Feed
Specification) and 'GBFS' (General Bikeshare Feed Specification) feeds
from agencies worldwide. Functions are designed to integrate seamlessly
with packages like 'tidytransit' and 'gtfstools' for subsequent feed
analysis.

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
