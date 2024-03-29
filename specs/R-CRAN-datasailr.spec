%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datasailr
%global packver   0.8.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.11
Release:          1%{?dist}%{?buildtag}
Summary:          Row by Row Data Processing Tool, Using 'DataSailr' Script

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    bison
BuildRequires:    flex
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
A row by row data processing tool. You can write data processing code in
'DataSailr' script which is specially intended for data manipulation. The
package uses 'libsailr' (C/C++ library) for its 'DataSailr' code parsing
and its execution.

%prep
%setup -q -c -n %{packname}
autoreconf -i %{packname}/src/Onigmo
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
