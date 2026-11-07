%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oddsapiio
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the 'Odds-API.io' Sports Betting Odds API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.1.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.1.0
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 

%description
Query live and upcoming sports betting odds from the 'Odds-API.io' REST
API <https://docs.odds-api.io>. Covers sports, markets, bookmakers,
leagues, participants, events, per-event and multi-event odds, odds
deltas, odds movements, odds summaries, value bets, arbitrage bets,
dropping odds, historical events, odds and closing lines, bet settlement
and grading, outright (futures) odds and results, and bookmaker id
mappings across 450+ bookmakers, returned as tidy data frames. An API key
from a paid plan is required.

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
