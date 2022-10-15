%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stopdetection
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stop Detection in Timestamped Trajectory Data using Spatiotemporal Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 

%description
Trajectory data formed by human or animal movement is often marked by
periods of movement interspersed with periods of standing still. It is
often of interest to researchers to separate geolocation trajectories of
latitude/longitude points by clustering consecutive locations to produce a
model of this behavior. This package implements the Stay Point detection
algorithm originally described in Ye (2009) <doi:10.1109/MDM.2009.11> that
uses time and distance thresholds to characterize spatial regions as
'stops'. This package also implements the concept of merging described in
Montoliu (2013) <doi:10.1007/s11042-011-0982-z> as stay point region
estimation, which allows for clustering of temporally adjacent stops for
which distance between the midpoints is less than the provided threshold.
GPS-like data from various sources can be used, but the temporal
thresholds must be considered with respect to the sampling interval, and
the spatial thresholds must be considered with respect to the measurement
error.

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
