%global __brp_check_rpaths %{nil}
%global packname  leafR
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates the Leaf Area Index (LAD) and Other Related Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-raster 
Requires:         R-stats 

%description
A set of functions for analyzing the structure of forests based on the
leaf area density (LAD) and leaf area index (LAI) measures calculated from
Airborne Laser Scanning (ALS), i.e., scanning lidar (Light Detection and
Ranging) data. The methodology is discussed and described in Almeida et
al. (2019) <doi:10.3390/rs11010092> and Stark et al. (2012)
<doi:10.1111/j.1461-0248.2012.01864.x>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
