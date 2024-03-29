%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SDLfilter
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Filtering and Assessing the Sample Size of Tracking Data

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-ggspatial 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-utils 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-ggspatial 

%description
Functions to filter GPS/Argos locations, as well as assessing the sample
size for the analysis of animal distributions. The filters remove temporal
and spatial duplicates, fixes located at a given height from estimated
high tide line, and locations with high error as described in Shimada et
al. (2012) <doi:10.3354/meps09747> and Shimada et al. (2016)
<doi:10.1007/s00227-015-2771-0>. Sample size for the analysis of animal
distributions can be assessed by the conventional area-based approach or
the alternative probability-based approach as described in Shimada et al.
(2021) <doi:10.1111/2041-210X.13506>.

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
