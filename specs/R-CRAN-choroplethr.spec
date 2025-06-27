%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  choroplethr
%global packver   5.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Color-Coded Choropleth Maps in R

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-tigris >= 1.0
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidycensus 
BuildRequires:    R-CRAN-rnaturalearth 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-tigris >= 1.0
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidycensus 
Requires:         R-CRAN-rnaturalearth 

%description
Easily create color-coded (choropleth) maps in R. No knowledge of
cartography or shapefiles needed; go directly from your geographically
identified data to a highly customizable map with a single line of code!
Supported geographies: U.S. states, counties, and census tracts, world
countries and sub-country regions (e.g., provinces, prefectures, etc.).
One of the suggested packages, rnaturalearthhires, is not available on
CRAN owing to its larger filesize (40MB). It can be installed from GitHub
using
remotes::install_github("https://github.com/ropensci/rnaturalearthhires").
This package contains higher resolution sub-country maps and is only
needed for the choropleth_admin1() function.

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
