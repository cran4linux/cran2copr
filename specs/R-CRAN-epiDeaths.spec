%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiDeaths
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Calculating Mortality Indicators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides functions for calculating mortality indicators. These include
geometric interpolation between two periods and projections for future
years, as described in the textbook by Laurenti, Mello Jorge, Lebrão and
Gotlieb (2005, ISBN:9788512408309), the standardised mortality ratio
(Bruce, Pope and Stanistreet, 2018, ISBN:9781118665411), the age-adjusted
mortality rate (direct standardisation), years of potential life lost
(Gardner and Sanborn, 1990, <doi:10.1097/00001648-199007000-00012>; Ma,
Ward, Siegel and Jemal, 2015, <doi:10.1001/jama.2015.12319>), and
age-standardised years of potential life lost (Silva Filho et al., 2024
<doi:10.1590/1413-81232024293.04702023EN>). Confidence intervals for the
standardised mortality ratio are obtained according to Vandenbroucke
(1982) <doi:10.1093/oxfordjournals.aje.a113306> and Ulm (1990)
<doi:10.1093/oxfordjournals.aje.a115507>. The function also includes a
function that produces a graph similar to an age pyramid.

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
