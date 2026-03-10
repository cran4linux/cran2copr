%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fozziejoin
%global packver   0.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Joining Dataframes with Inexact Matching

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cargo
BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Provides functions for joining data frames based on inexact criteria,
including string distance, Manhattan distance, Euclidean distance, and
interval overlap. This API is designed as a modern, performance-oriented
alternative to the 'fuzzyjoin' package (Robinson 2026)
<doi:10.32614/CRAN.package.fuzzyjoin>. String distance functions utilizing
'q-grams' are adapted with permission from the 'textdistance' 'Rust' crate
(Orsinium 2024) <https://docs.rs/textdistance/latest/textdistance/>. Other
string distance calculations rely on the 'rapidfuzz' 'Rust' crate
(Bachmann 2023) <https://docs.rs/rapidfuzz/0.5.0/rapidfuzz/>. Interval
joins are backed by a Adelson-Velsky and Landis tree as implemented by the
'interavl' 'Rust' crate <https://docs.rs/interavl/0.5.0/interavl/>.

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
