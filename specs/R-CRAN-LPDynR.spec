%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LPDynR
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Land Productivity Dynamics Indicator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-virtualspecies 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-terra 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-virtualspecies 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-terra 

%description
It uses 'phenological' and productivity-related variables derived from
time series of vegetation indexes, such as the Normalized Difference
Vegetation Index, to assess ecosystem dynamics and change, which
eventually might drive to land degradation. The final result of the Land
Productivity Dynamics indicator is a categorical map with 5 classes of
land productivity dynamics, ranging from declining to increasing
productivity. See
www.sciencedirect.com/science/article/pii/S1470160X21010517/ for a
description of the methods used in the package to calculate the indicator.

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
