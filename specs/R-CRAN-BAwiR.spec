%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BAwiR
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Basketball Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Anthropometry 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-Anthropometry 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xml2 

%description
Collection of tools to work with European basketball data. Functions
available are related to friendly web scraping, data management and
visualization. Data were obtained from
<https://www.euroleaguebasketball.net/euroleague/>,
<https://www.euroleaguebasketball.net/eurocup/> and
<https://www.acb.com/>, following the instructions of their respectives
robots.txt files, when available. Box score data are available for the
three leagues. Play-by-play data are also available for the Spanish
league. Methods for analysis include a population pyramid, 2D plots,
circular plots of players' percentiles, plots of players' monthly/yearly
stats, team heatmaps, team shooting plots, team four factors plots,
cross-tables with the results of regular season games, maps of
nationalities, combinations of lineups, possessions-related variables,
timeouts, performance by periods, personal fouls and offensive rebounds.
Please see Vinue (2020) <doi:10.1089/big.2018.0124>.

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
