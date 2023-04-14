%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  almanac
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with Recurrence Rules

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-V8 >= 4.2.2
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-vctrs >= 0.6.1
Requires:         R-CRAN-V8 >= 4.2.2
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-vctrs >= 0.6.1

%description
Provides tools for defining recurrence rules and recurrence sets.
Recurrence rules are a programmatic way to define a recurring event, like
the first Monday of December. Multiple recurrence rules can be combined
into larger recurrence sets. A full holiday and calendar interface is also
provided that can generate holidays within a particular year, can detect
if a date is a holiday, can respect holiday observance rules, and allows
for custom holidays.

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
