%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smosr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Acquire and Explore BEC-SMOS L4 Soil Moisture Data in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Provides functions that automate accessing, downloading and exploring Soil
Moisture and Ocean Salinity (SMOS) Level 4 (L4) data developed by
Barcelona Expert Center (BEC). Particularly, it includes functions to
search for, acquire, extract, and plot BEC-SMOS L4 soil moisture data
downscaled to ~1 km spatial resolution. Note that SMOS is one of Earth
Explorer Opportunity missions by the European Space Agency (ESA). More
information about SMOS products can be found at
<https://earth.esa.int/eogateway/missions/smos/data>.

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
