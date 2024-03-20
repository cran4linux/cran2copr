%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dendRoAnalyst
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Processing and Analyzing Dendrometer Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-base 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-stringr 

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
