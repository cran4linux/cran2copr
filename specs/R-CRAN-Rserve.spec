%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rserve
%global packver   1.8-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.16
Release:          1%{?dist}%{?buildtag}
Summary:          Versatile R Server

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.5.0
Requires:         R-core >= 1.5.0

%description
Rserve is a versatile, scalable server enabling the efficient use of R
from other applications through variety of protocols including QAP,
WebSockets, HTTP and HTTPS. It acts as a server (TCP/IP or local sockets)
which allows binary requests to be sent to R. Every connection has a
separate workspace and working directory. Client-side implementations are
available for many popular languages allowing applications to use
facilities of R without the need of linking to the R binary. Rserve
supports remote connections, user authentication and file transfer. A
simple R client is included in this package as well. It also supports OCAP
mode for secure remote procedure calls, including support for full event
loop, asynchronous results/graphics and console I/O.

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
