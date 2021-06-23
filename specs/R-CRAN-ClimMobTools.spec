%global __brp_check_rpaths %{nil}
%global packname  ClimMobTools
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          API Client for the 'ClimMob' Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-climatrends 
BuildRequires:    R-CRAN-PlackettLuce 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-climatrends 
Requires:         R-CRAN-PlackettLuce 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-RSpectra 

%description
API client for 'ClimMob', an open source software for experimental
crowdsourcing citizen science under the 'tricot' approach
<https://climmob.net/>. Developed by van Etten et al. (2019)
<doi:10.1017/S0014479716000739>, it turns the research paradigm on its
head; instead of a few researchers designing complicated trials to compare
several technologies in search of the best solutions for the target
environment, it enables many participants to carry out reasonably simple
experiments that taken together can offer even more information.
'ClimMobTools' enables project managers to deep explore and analyse their
'ClimMob' data in R.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
