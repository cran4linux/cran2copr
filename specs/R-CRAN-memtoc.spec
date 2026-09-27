%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  memtoc
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Tictoc'-Style Memory Usage Tracking

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.7.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-ps >= 1.7.0
Requires:         R-CRAN-callr >= 3.7.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-ps >= 1.7.0

%description
Provides simple start/stop memory tracking functions tic_mem() and
toc_mem() that can be nested, inspired by the 'tictoc' package. Track RAM
usage during code execution with support for logging, custom messages,
nested tracking blocks, and parallel worker monitoring. Features
continuous background polling to estimate peak memory usage across main
process and workers. Integrates with the 'future' package ecosystem for
automatic worker detection. Designed for monitoring memory consumption in
parallel workflows.

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
