%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timetools
%global packver   1.15.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15.4
Release:          1%{?dist}%{?buildtag}
Summary:          Seasonal/Sequential (Instants/Durations, Even or not) Time Series

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Objects to manipulate sequential and seasonal time series. Sequential time
series based on time instants and time duration are handled. Both can be
regularly or unevenly spaced (overlapping duration are allowed). Only
POSIX* format are used for dates and times. The following classes are
provided : 'POSIXcti', 'POSIXctp', 'TimeIntervalDataFrame',
'TimeInstantDataFrame', 'SubtimeDataFrame' ; methods to switch from a
class to another and to modify the time support of series (hourly time
series to daily time series for instance) are also defined. Tools provided
can be used for instance to handle environmental monitoring data (not
always produced on a regular time base).

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
