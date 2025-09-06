%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ndi
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Neighborhood Deprivation Indices

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidycensus 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tigris 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidycensus 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tigris 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
Computes various geospatial indices of socioeconomic deprivation and
disparity in the United States. Some indices are considered "spatial"
because they consider the values of neighboring (i.e., adjacent) census
geographies in their computation, while other indices are "aspatial"
because they only consider the value within each census geography. Two
types of aspatial neighborhood deprivation indices (NDI) are available:
including: (1) based on Messer et al. (2006)
<doi:10.1007/s11524-006-9094-x> and (2) based on Andrews et al. (2020)
<doi:10.1080/17445647.2020.1750066> and Slotman et al. (2022)
<doi:10.1016/j.dib.2022.108002> who use variables chosen by Roux and Mair
(2010) <doi:10.1111/j.1749-6632.2009.05333.x>. Both are a decomposition of
multiple demographic characteristics from the U.S. Census Bureau American
Community Survey 5-year estimates (ACS-5; 2006-2010 onward). Using data
from the ACS-5 (2005-2009 onward), the package can also compute indices of
racial or ethnic residential segregation, including but limited to those
discussed in Massey & Denton (1988) <doi:10.1093/sf/67.2.281>, and
additional indices of socioeconomic disparity.

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
