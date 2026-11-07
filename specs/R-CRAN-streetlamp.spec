%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  streetlamp
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Econometrics for the Effect of Police Stop and Search on Recorded Crime

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-did 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-did 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-generics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Builds an area-by-month panel of recorded crime in England and Wales from
the data.police.uk bulk archive <https://data.police.uk/data/archive/>,
attaches stop and search intensity as a treatment variable, and provides a
panel-econometrics toolkit for evaluating policing interventions: two-way
fixed effects, event studies, difference-in-differences with staggered
adoption, synthetic control, spatial spillover and displacement models,
and stop-crime elasticities by offence type. Area boundaries are read from
the Office for National Statistics Open Geography Portal
<https://geoportal.statistics.gov.uk/>, Census 2021 population from the
'Nomis' API <https://www.nomisweb.co.uk/api/v01/help>, and notes of
re-supplied and missing force data from the data.police.uk change log
<https://data.police.uk/changelog/>. Every panel carries a contract
recording provenance, coverage, geography vintage and treatment
definition; every estimator names its identifying assumption and ships
with a placebo or pre-trend diagnostic.

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
