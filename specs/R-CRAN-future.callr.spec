%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  future.callr
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Future API for Parallel Processing using 'callr'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.58.0
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-callr 
Requires:         R-CRAN-future >= 1.58.0
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-callr 

%description
Implementation of the Future API <doi:10.32614/RJ-2021-048> on top of the
'callr' package.  This allows you to process futures, as defined by the
'future' package, in parallel out of the box, on your local (Linux, macOS,
Windows, ...) machine.  Contrary to backends relying on the 'parallel'
package (e.g. 'future::multisession') and socket connections, the 'callr'
backend provided here can run more than 125 parallel R processes.

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
