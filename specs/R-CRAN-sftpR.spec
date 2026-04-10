%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sftpR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust SFTP Interface Using 'curl'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 7.0.0
BuildRequires:    R-CRAN-R6 >= 2.6.1
Requires:         R-CRAN-curl >= 7.0.0
Requires:         R-CRAN-R6 >= 2.6.1

%description
Provides a high-level, object-oriented interface for Secure File Transfer
Protocol (SFTP) operations built upon the 'curl' package. The package
implements an 'R6' class to manage persistent connections and provides
'tidyverse'-style functions for common file system tasks. Key features
include recursive directory creation with idempotency support, "smart"
local path resolution that distinguishes between files and directories,
and the ability to download remote resources directly into memory as raw
vectors for seamless integration into data processing pipelines. It is
designed to handle common SFTP edge cases gracefully, providing
informative error messages and robust path sanitization to ensure
compatibility across different server configurations.

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
