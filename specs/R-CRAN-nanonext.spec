%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nanonext
%global packver   1.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight Toolkit for Messaging, Concurrency and the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6

%description
R binding for NNG (Nanomsg Next Gen), a successor to ZeroMQ. A toolkit for
messaging, concurrency and the web. High-performance socket messaging over
in-process, IPC, TCP, WebSocket and secure TLS transports implements
'Scalability Protocols', a standard for common communications patterns
including publish/subscribe, request/reply and survey. A threaded
concurrency framework with intuitive 'aio' objects that resolve
automatically upon completion of asynchronous operations, and
synchronisation primitives that allow R to wait on events signalled by
concurrent threads. A unified HTTP server hosting REST endpoints,
WebSocket connections and streaming on a single port, with a built-in HTTP
client.

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
