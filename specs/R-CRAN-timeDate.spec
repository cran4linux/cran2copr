%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timeDate
%global packver   4032.109
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4032.109
Release:          1%{?dist}%{?buildtag}
Summary:          Rmetrics - Chronological and Calendar Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 

%description
The 'timeDate' class fulfils the conventions of the ISO 8601 standard as
well as of the ANSI C and POSIX standards. Beyond these standards it
provides the "Financial Center" concept which allows to handle data
records collected in different time zones and mix them up to have always
the proper time stamps with respect to your personal financial center, or
alternatively to the GMT reference time. It can thus also handle time
stamps from historical data records from the same time zone, even if the
financial centers changed day light saving times at different calendar
dates.

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
