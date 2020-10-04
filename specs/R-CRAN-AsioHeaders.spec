%global packname  AsioHeaders
%global packver   1.16.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          'Asio' C++ Header Files

License:          BSL-1.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model
using a modern C++ approach. It is also included in Boost but requires
linking when used with Boost. Standalone it can be used header-only
(provided a recent compiler). 'Asio' is written and maintained by
Christopher M. Kohlhoff, and released under the 'Boost Software License',
Version 1.0.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
