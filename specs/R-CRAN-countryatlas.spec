%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  countryatlas
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Join World Bank Data, Country Codes and Maps on the ISO Spine

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-WDI 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-WDI 

%description
A complete toolkit for getting country data onto honest maps. Country
names rarely line up across data sources ("US", "U.S.", "United States",
"United States of America" are one country, but a naive join treats them
as four), so 'countryatlas' makes ISO codes the universal join key. It
generalises a one-call, map-ready table that stitches together 'ggplot2'
map geometry, 'WDI' World Bank indicators and the 'countrycode' Rosetta
stone; exposes the join machinery for the user's own data; ships curated
reference data (metadata, group memberships, an indicator catalogue, flags
and currencies); adds analysis helpers (per-capita, regional roll-ups,
ranking); and turns one hand-drawn choropleth into a full vocabulary of
projected, area-honest maps (binned and quantile choropleths,
proportional-symbol, bivariate, cartogram, tile-grid, flow, animated and
interactive). Heavy spatial dependencies stay optional, and a bundled
offline snapshot lets every example, test and vignette run without the
network.

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
