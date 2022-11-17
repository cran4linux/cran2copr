%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dendRoAnalyst
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Processing and Analyzing Dendrometer Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-base 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-zoo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-base 

%description
There are various functions for managing and cleaning data before the
application of different approaches. This includes identifying and erasing
sudden jumps in dendrometer data not related to environmental change,
identifying the time gaps of recordings, and changing the temporal
resolution of data to different frequencies. Furthermore, the package
calculates daily statistics of dendrometer data, including the daily
amplitude of tree growth. Various approaches can be applied to separate
radial growth from daily cyclic shrinkage and expansion due to uptake and
loss of stem water. In addition, it identifies periods of consecutive days
with user-defined climatic conditions in daily meteorological data, then
check what trees are doing during that period.

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
