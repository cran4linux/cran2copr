%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  distrSim
%global packver   2.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation Classes Based on Package 'distr'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-setRNG >= 2006.2.1
BuildRequires:    R-CRAN-distr >= 2.5.2
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-setRNG >= 2006.2.1
Requires:         R-CRAN-distr >= 2.5.2
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-startupmsg 
Requires:         R-stats 
Requires:         R-grDevices 

%description
S4-classes for setting up a coherent framework for simulation within the
distr family of packages.

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
