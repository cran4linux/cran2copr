%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greenSD
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Analyze Global GreenSpace Spatial Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-maptiles 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-nominatimlite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dsmSearch 
BuildRequires:    R-CRAN-rstac 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-maptiles 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-nominatimlite 
Requires:         R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dsmSearch 
Requires:         R-CRAN-rstac 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-aws.s3 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 

%description
Access and analyze multi-band greenspace seasonality data cubes (available
for 1,028 major global cities), global Normalized Difference Vegetation
Index / land cover data from the European Space Agency WorldCover 10m
Dataset, and Sentinel-2-l2a images. Users can download data using bounding
boxes, city names, and filter by year or seasonal time window. The package
also supports calculating human exposure to greenspace using a
population-weighted greenspace exposure model introduced by Chen et al.
(2022) <doi:10.1038/s41467-022-32258-4> based on Global Human Settlement
Layer population data, and calculating a set of greenspace morphology
metrics at patch and landscape levels.

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
