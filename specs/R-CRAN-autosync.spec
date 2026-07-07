%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autosync
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Automerge' Sync Server and Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-nanonext >= 1.8.1
BuildRequires:    R-CRAN-secretbase >= 1.3.0
BuildRequires:    R-CRAN-httr2 >= 1.2.3
BuildRequires:    R-CRAN-automerge >= 0.4.0
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-promises 
Requires:         R-CRAN-nanonext >= 1.8.1
Requires:         R-CRAN-secretbase >= 1.3.0
Requires:         R-CRAN-httr2 >= 1.2.3
Requires:         R-CRAN-automerge >= 0.4.0
Requires:         R-CRAN-jose 
Requires:         R-CRAN-later 
Requires:         R-CRAN-promises 

%description
A WebSocket-based implementation of the 'automerge-repo' synchronization
protocol used by 'sync.automerge.org'. Acts as a sync server, enabling 'R'
to serve as a synchronization hub for 'Automerge' clients in 'JavaScript',
'Rust', and other languages, and as a client for fetching, editing, and
synchronizing documents hosted on remote servers.

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
