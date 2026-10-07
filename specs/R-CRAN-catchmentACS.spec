%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  catchmentACS
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Isochrone-Based Area-Weighted ACS Aggregation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidycensus >= 1.6
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tigris 
Requires:         R-CRAN-tidycensus >= 1.6
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tigris 

%description
Computes American Community Survey (ACS) estimates for the area within a
given drive time of each of a set of points, such as the locations of
pre-kindergarten classrooms. Such an area is called an isochrone. The
drive-time areas come from a routing service, either the 'Open Source
Routing Machine' ('OSRM', <https://project-osrm.org/>) or
'openrouteservice' (<https://openrouteservice.org/>), and the ACS 5-year
estimates of census tracts come from the Census Bureau
(<https://www.census.gov/data/developers.html>) through the 'tidycensus'
package, one state at a time. The tracts that overlap an area are combined
by area weighting, which uses two weights: the share of each tract's area
that lies inside, for counts and rates, and each tract's share of the
overlapping area, for the medians and per-person values of three ACS
tables (median household income, median home value, and per capita
income). A median or per-person value from any other table is added up
like a count. Counts, medians, per-person values, and five rates are
returned with a margin of error at a chosen confidence level, 90 percent
by default, and with a record of the settings, inputs, and package
versions behind the run. The five rates are the poverty rate, the shares
of households receiving Supplemental Nutrition Assistance Program (SNAP)
benefits and Supplemental Security Income, the unemployment rate, and the
labor force participation rate. The margins of error of counts and rates
use the approximation formulas in chapter 8 of U.S. Census Bureau (2020)
"Understanding and Using American Community Survey Data: What All Data
Users Need to Know"
<https://www.census.gov/programs-surveys/acs/library/handbooks/general.html>.
For a count the formula for a sum is applied to the weighted tract
estimates, with the weights treated as fixed. For a rate the default is
the formula for a ratio. Its margin of error is at least as wide as that
of the formula for a proportion, which the handbook gives for ratios whose
numerator is part of the denominator, as it is in all five rates. The
margins of error of medians and per-person values are an approximation
made by the package.

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
