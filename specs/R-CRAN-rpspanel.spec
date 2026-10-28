%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rpspanel
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          US State Energy-Economy Panels with Renewable Portfolio Standards

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Builds a documented, reproducible state-by-year panel for the 50 US states
and the District of Columbia that combines energy consumption, prices and
production from the US Energy Information Administration (EIA) State
Energy Data System, electricity generation and retail sales, state
energy-related carbon dioxide emissions, and state GDP, income and
population from the Bureau of Economic Analysis (BEA). Data are downloaded
on demand through the official APIs and cached locally, with the source,
vintage and transformation of every variable recorded in a codebook.
Renewable Portfolio Standard (RPS) rules are turned into standardised
annual stringency indices (adoption, nominal, coverage-adjusted and
incremental requirements, following Yin and Powers (2010)
<doi:10.1016/j.enpol.2009.10.067>, plus design-flexibility indicators).
Output works directly with the 'plm', 'fixest' and 'csdm' packages.

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
