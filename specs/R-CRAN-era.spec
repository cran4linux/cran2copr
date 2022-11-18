%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  era
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Year-Based Time Scales

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pillar 
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pillar 

%description
Provides a consistent representation of year-based time scales as a
numeric vector with an associated 'era'. There are built-in era
definitions for many year numbering systems used in contemporary and
historic calendars (e.g. Common Era, Islamic 'Hijri' years); year-based
time scales used in archaeology, astronomy, geology, and other
palaeosciences (e.g. Before Present, SI-prefixed 'annus'); and support for
arbitrary user-defined eras. Years can converted from any one era to
another using a generalised transformation function. Methods are also
provided for robust casting and coercion between years and other numeric
types, type-stable arithmetic with years, and pretty-printing in tables.

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
