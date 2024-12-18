%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rserve
%global packver   1.8-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.15
Release:          1%{?dist}%{?buildtag}
Summary:          Versatile R Server

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.5.0
Requires:         R-core >= 1.5.0

%description
Rserve acts as a socket server (TCP/IP or local sockets) which allows
binary requests to be sent to R. Every connection has a separate workspace
and working directory. Client-side implementations are available for
popular languages such as C/C++ and Java, allowing any application to use
facilities of R without the need of linking to R code. Rserve supports
remote connection, user authentication and file transfer. A simple R
client is included in this package as well. In addition, it can also act
as a secure WebSockets and HTTP/HTTPS server.

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
