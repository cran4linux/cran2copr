%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lakemorpho
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lake Morphometry Metrics

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-cluster 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-cluster 

%description
Lake morphometry metrics are used by limnologists to understand, among
other things, the ecological processes in a lake. Traditionally, these
metrics are calculated by hand, with planimeters, and increasingly with
commercial GIS products. All of these methods work; however, they are
either outdated, difficult to reproduce, or require expensive licenses to
use. The 'lakemorpho' package provides the tools to calculate a typical
suite of these metrics from an input elevation model and lake polygon. The
metrics currently supported are: fetch, major axis, minor axis,
major/minor axis ratio, maximum length, maximum width, mean width, maximum
depth, mean depth, shoreline development, shoreline length, surface area,
and volume.

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
