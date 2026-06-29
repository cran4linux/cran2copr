%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixtime
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Temporal Vectors and Operations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-vecvec >= 1.2.0
BuildRequires:    R-CRAN-cpp11 >= 0.5.2
BuildRequires:    R-CRAN-tzdb >= 0.5.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-methods 
Requires:         R-CRAN-vecvec >= 1.2.0
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-tzdb >= 0.5.0
Requires:         R-methods 

%description
Flexible time classes for time series analysis and forecasting with mixed
temporal granularities. Supports linear and cyclical time representations
in discrete and continuous forms, with timezone support, across multiple
calendar systems including Gregorian and ISO week date calendars. Time
points are stored numerically relative to a chronon; an atomic time
granule defined by time units of a calendar. Calendrical arithmetic
enables conversion between time granules (e.g. days to months) and
calendar systems. Multi-unit arithmetic allows for temporal analysis with
other granules of common calendars (e.g. fortnights are 2-week units).
Time vectors of different granularities (e.g. monthly and quarterly) can
be combined in a single vector, making 'mixtime' ideal for data that
changes observation frequency over time or requires temporal
reconciliation across scales. The package is extensible, allowing users to
define custom calendars that build upon civil and astronomical time
systems.

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
