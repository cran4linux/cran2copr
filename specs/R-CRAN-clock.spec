%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clock
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Date-Time Types and Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-cli >= 3.6.4
BuildRequires:    R-CRAN-rlang >= 1.1.5
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-vctrs >= 0.6.5
BuildRequires:    R-CRAN-cpp11 >= 0.5.2
BuildRequires:    R-CRAN-tzdb >= 0.5.0
Requires:         R-CRAN-cli >= 3.6.4
Requires:         R-CRAN-rlang >= 1.1.5
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-vctrs >= 0.6.5
Requires:         R-CRAN-tzdb >= 0.5.0

%description
Provides a comprehensive library for date-time manipulations using a new
family of orthogonal date-time classes (durations, time points,
zoned-times, and calendars) that partition responsibilities so that the
complexities of time zones are only considered when they are really
needed. Capabilities include: date-time parsing, formatting, arithmetic,
extraction and updating of components, and rounding.

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
