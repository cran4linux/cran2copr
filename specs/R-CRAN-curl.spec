%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  curl
%global packver   5.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Modern and Flexible Web Client for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libcurl-devel
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
The curl() and curl_download() functions provide highly configurable
drop-in replacements for base url() and download.file() with better
performance, support for encryption (https, ftps), gzip compression,
authentication, and other 'libcurl' goodies. The core of the package
implements a framework for performing fully customized requests where data
can be processed either in memory, on disk, or streaming via the callback
or connection interfaces. Some knowledge of 'libcurl' is recommended; for
a more-user-friendly web client see the 'httr' package which builds on
this package with http specific tools and logic.

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
