%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sage
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve Slices of the Small-Area Global Elections Archive

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow >= 14.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-arrow >= 14.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Downloads and subsets slices of the Small-Area Global Elections (SAGE)
archive, a harmonized collection of polling-station and precinct-level
election results, without having to read monolithic country-level files.
Reads partitioned 'Parquet' from a public bucket (configurable through the
'SAGE_SOURCE' environment variable, the 'sage_set_source()' function, or a
local copy of the archive) and exposes a 'sage_load(country, years,
columns)' function returning a 'tibble', plus helpers for the accompanying
boundary polygons and candidate-level vote sidecars. See
<https://github.com/noahdasanaike/sage> for the archive itself.

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
