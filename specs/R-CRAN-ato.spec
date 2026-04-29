%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ato
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Tidy Australian Taxation Office Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-readxl >= 1.4.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-readxl >= 1.4.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-tools 
Requires:         R-utils 

%description
Fetch Australian Taxation Office ('ATO') Taxation Statistics and related
datasets via the 'data.gov.au' Comprehensive Knowledge Archive Network
('CKAN') API <https://data.gov.au/data/api/3/>. Provides tidy access to
individual, company, superannuation, goods and services tax ('GST'),
fringe benefits tax ('FBT'), Voluntary Tax Transparency Code ('VTTC'), Pay
As You Go ('PAYG') withholding, charity, excise, and Corporate Tax
Transparency data, plus Division 293, Petroleum Resource Rent Tax,
Medicare Levy Surcharge, fuel tax credits, compliance, and Working Holiday
Maker aggregates. Includes reproducibility helpers (snapshot pinning,
SHA-256 cache integrity, session manifest, optional 'Zenodo' deposit),
classification crosswalks ('ANZSIC' 2006 to 2020, 'ANZSCO' 2013 to 2021),
panel harmonisation, reconciliation against Final Budget Outcome totals,
and real-terms and per-capita helpers backed by bundled Australian Bureau
of Statistics ('ABS') Consumer Price Index and Estimated Resident
Population series. Bridges to the 'taxstats' 2 per cent microdata sample
via column-schema mapping. Data is published by the Australian Taxation
Office under Creative Commons Attribution 2.5 Australia or 3.0 Australia
licences (dataset-dependent).

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
