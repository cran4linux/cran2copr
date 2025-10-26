%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  latbias
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Latitudinal Bias Index

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.3
Requires:         R-core >= 3.5.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-units 

%description
Studies that report shifts in species distributions may be biased by the
shape of the study area. The main functionality of this package is to
calculate the Latitudinal Bias Index (LBI) for any given shape. The LBI is
bounded between +1 (100%% probability to exclusively record latitudinal
shifts, i.e., range shifts data sampled along a perfectly South-North
oriented straight line) and -1 (100%% probability to exclusively record
longitudinal shifts, i.e., range shifts data sampled along a perfectly
East-West oriented straight line).

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
