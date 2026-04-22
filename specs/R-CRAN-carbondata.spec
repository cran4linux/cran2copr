%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  carbondata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Carbon Market Data from Emissions Trading Systems and Voluntary Registries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readxl 
Requires:         R-tools 
Requires:         R-utils 

%description
Unified access to carbon market data from compliance emissions trading
systems ('EU ETS', 'UK ETS', 'RGGI', California Cap-and-Trade) and
voluntary carbon markets (Verra, Gold Standard, American Carbon Registry,
Climate Action Reserve, via the Berkeley Voluntary Registry Offsets
Database and the 'CarbonPlan' 'OffsetsDB' API). Includes cross-market
price data from the 'International Carbon Action Partnership' ('ICAP')
Allowance Price Explorer <https://icapcarbonaction.com/en/ets-prices>,
global carbon pricing from the World Bank Carbon Pricing Dashboard
<https://carbonpricingdashboard.worldbank.org/>, and the historical 'RFF'
World Carbon Pricing Database following Dolphin, Pollitt and Newbery
(2020) <doi:10.1038/s41597-022-01659-x>. Data is downloaded from public
sources on first use and cached locally.

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
