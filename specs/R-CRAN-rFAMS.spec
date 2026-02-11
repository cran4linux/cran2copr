%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rFAMS
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fisheries Analysis and Modeling Simulator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-FSA 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-FSA 

%description
Simulates the dynamics of exploited fish populations using the Jones
modification of the Beverton-Holt equilibrium yield equation to compute
yield-per-recruit and dynamic pool models (Ricker 1975)
<https://publications.gc.ca/site/eng/480738/publication.html>. Allows
users to evaluate minimum, slot, and inverted length limits on exploited
fisheries using specified life history parameters. Users can simulate
population under a variety of conditional fishing mortality and
conditional natural mortality. Calculated quantities include number of
fish harvested and dying naturally, mean weight and length of fish
harvested, number of fish that reach specified lengths of interest, total
number of fish and biomass in the population, and stock density indices.

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
