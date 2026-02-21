%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fauxpas
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          HTTP Error Helpers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-httpcode >= 0.3.0
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-httpcode >= 0.3.0
Requires:         R-CRAN-whisker 

%description
HTTP error helpers. Methods included for general purpose HTTP error
handling, as well as individual methods for every HTTP status code, both
via status code numbers as well as their descriptive names. Supports
ability to adjust behavior to stop, message or warning. Includes ability
to use custom whisker template to have any configuration of status code,
short description, and verbose message. Currently supports integration
with 'crul', 'curl', and 'httr'.

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
