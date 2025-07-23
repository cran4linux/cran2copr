%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Tivy
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing and Analysis of Peruvian Fishery Logbook Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-pdftools >= 3.0.0
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-future.apply >= 1.7.0
BuildRequires:    R-CRAN-jsonlite >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-stringi >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-future >= 1.21.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.0
BuildRequires:    R-CRAN-patchwork >= 1.1.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-pdftools >= 3.0.0
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-future.apply >= 1.7.0
Requires:         R-CRAN-jsonlite >= 1.6.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-stringi >= 1.4.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-future >= 1.21.0
Requires:         R-CRAN-RColorBrewer >= 1.1.0
Requires:         R-CRAN-patchwork >= 1.1.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-stats 
Requires:         R-utils 

%description
Specialized toolkit for processing biological and fisheries data from
Peru's anchovy (Engraulis ringens) fishery. Provides functions to analyze
fishing logbooks, calculate biological indicators (length-weight
relationships, juvenile percentages), generate spatial fishing indicators,
and visualize regulatory measures from Peru's Ministry of Production.
Features automated data processing from multiple file formats, coordinate
validation, spatial analysis of fishing zones, and tools for analyzing
fishing closure announcements and regulatory compliance. Includes built-in
datasets of Peruvian coastal coordinates and parallel lines for analyzing
fishing activities within regulatory zones.

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
