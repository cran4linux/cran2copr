%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  paisaje
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Environmental Data Tools for Landscape Ecology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-h3jsr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-spocc 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-h3jsr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-spocc 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-magrittr 

%description
Provides functions for landscape analysis and data retrieval. The package
allows users to download environmental variables from global datasets
(e.g., WorldClim, ESA WorldCover, Nighttime Lights), and to compute
spatial and landscape metrics using a hexagonal grid system based on the
H3 spatial index. It is useful for ecological modeling, biodiversity
studies, and spatial data processing in landscape ecology. Fick and
Hijmans (2017) <doi:10.1002/joc.5086>. Zanaga et al. (2022)
<doi:10.5281/zenodo.7254221>. Uber Technologies Inc. (2022) "H3: Hexagonal
hierarchical spatial index".

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
