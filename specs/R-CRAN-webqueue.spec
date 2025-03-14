%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  webqueue
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multicore HTTP Server

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jobqueue 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-semaphore 
BuildRequires:    R-CRAN-webutils 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jobqueue 
Requires:         R-CRAN-later 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-semaphore 
Requires:         R-CRAN-webutils 
Requires:         R-utils 

%description
Distributes HTTP requests among a pool of background R processes. Supports
timeouts and interrupts of requests to ensure that CPU cores are utilized
effectively.

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
