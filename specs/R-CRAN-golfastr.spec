%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  golfastr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficiently Access Pro Golf Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-cli 

%description
Designed for quickly grabbing PGA Tour data. Includes a large data update
with shot-level PGA Tour 'ShotLink' data, tee times and course setup,
strokes gained, win probability after every hole, a what's in the bag
database (WITBDB) of player equipment, an ID crosswalk between 'ESPN' and
the PGA Tour, and logo image URLs. Leaderboards and hole-by-hole scoring
come from 'ESPN' <https://www.espn.com/golf/> for the PGA Tour, LIV Golf,
LPGA, DP World Tour and Champions Tour. Completed seasons are served from
hosted files for fast repeated access, and data can be saved as RDS,
'Apache Arrow' Parquet or a 'SQLite' database.

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
