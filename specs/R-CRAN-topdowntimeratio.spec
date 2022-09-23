%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  topdowntimeratio
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Top-Down Time Ratio Segmentation for Coordinate Trajectories

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-geodist >= 0.0.4
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-geodist >= 0.0.4
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 

%description
Data collected on movement behavior is often in the form of time- stamped
latitude/longitude coordinates sampled from the underlying movement
behavior. These data can be compressed into a set of segments via the Top-
Down Time Ratio Segmentation method described in Meratnia and de By (2004)
<doi:10.1007/978-3-540-24741-8_44> which, with some loss of information,
can both reduce the size of the data as well as provide corrective
smoothing mechanisms to help reduce the impact of measurement error.  This
is an improvement on the well-known Douglas-Peucker algorithm for
segmentation that operates not on the basis of perpendicular distances.
Top-Down Time Ratio segmentation allows for disparate sampling time
intervals by calculating the distance between locations and segments with
respect to time. Provided a trajectory with timestamps, tdtr() returns a
set of straight- line segments that can represent the full trajectory.
McCool, Lugtig, and Schouten (2022) <doi:10.1007/s11116-022-10328-2>
describe this method as implemented here in more detail.

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
