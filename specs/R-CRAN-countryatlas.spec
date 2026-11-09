%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  countryatlas
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Join World Bank Data, Country Codes and Maps on the ISO Spine

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-WDI 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-memoise 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-WDI 

%description
A complete toolkit for getting country data onto honest maps. Country
names rarely line up across data sources ("US", "U.S.", "United States",
"United States of America" are one country, but a naive join treats them
as four), so 'countryatlas' makes ISO codes the universal join key, and
matches names in many languages. It joins indicators from the World Bank,
Our World in Data, the European Union's statistical office and any
statistical data and metadata exchange service to bundled Natural Earth
borders and the 'countrycode' Rosetta stone, recording each value's
source, unit and release, and can pin a World Bank release so a result
reproduces; treats country-year panels as first class, with dated income
groups, regions and group memberships, lags keyed on the year and
aggregates that report their coverage; adds analysis helpers (per-capita,
inequality, convergence, distribution dynamics, rates, and spatial
statistics with multiple-testing control); and draws a full vocabulary of
equal-area maps (classed and continuous choropleths, proportional-symbol,
spike, bivariate, ternary, value-by-alpha, cartogram, tile-grid, flow,
small-multiple, animated, globe and interactive), and can hand its curated
tables to 'ggsql' for database-side rendering. Honesty is treated as a
feature rather than a slogan: maps state their coverage and source, draw
small states rather than dropping them and describe themselves in alt
text, classification methods can be compared side by side, and the
distortion each projection introduces can be measured and drawn. Heavy
spatial dependencies stay optional, and a bundled offline snapshot lets
every example, test and vignette run without the network.

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
