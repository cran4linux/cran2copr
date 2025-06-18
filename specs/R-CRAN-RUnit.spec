%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RUnit
%global packver   0.4.33.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.33.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Unit Test Framework

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-utils >= 2.5.0
BuildRequires:    R-methods >= 2.5.0
BuildRequires:    R-graphics >= 2.5.0
Requires:         R-utils >= 2.5.0
Requires:         R-methods >= 2.5.0
Requires:         R-graphics >= 2.5.0

%description
R functions implementing a standard Unit Testing framework, with
additional code inspection and report generation tools.

%prep
%setup -q -c -n %{packname}
sed -i '/Sexpr/d' %{packname}/man/checkFuncs.Rd
 sed -i 's/"runitVirtualClassTest.r")}/"runitVirtualClassTest.r"/g' %{packname}/man/checkFuncs.Rd
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
