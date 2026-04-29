%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Tidy Australian Clean Energy Regulator Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-readxl >= 1.4.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-readxl >= 1.4.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-tools 
Requires:         R-utils 

%description
Fetch Australian Clean Energy Regulator data on carbon credits, safeguard
mechanism facilities, renewable energy certificates, and greenhouse gas
reporting. Provides tidy access to the Australian Carbon Credit Unit
('ACCU') Scheme project register, Safeguard Mechanism baselines and
covered emissions, Large-scale Renewable Energy Target ('LRET') power
station accreditations, Small-scale Renewable Energy Scheme ('SRES')
installation data, the National Greenhouse and Energy Reporting ('NGER')
scheme, and Quarterly Carbon Market Reports
<https://cer.gov.au/markets/reports-and-data>. Includes a post-Chubb ACCU
integrity layer (Chubb 2022 Independent Review), Safeguard reform handling
(declining industry baselines from July 2023), National Greenhouse and
Energy Reporting scope discipline (Scope 1 / Scope 2 market vs location /
Climate Active), reconciliation against the Quarterly Carbon Market
Report, and reproducibility helpers (snapshot pinning, SHA-256 cache
integrity, session manifest, optional Zenodo deposit). Data is published
by the Clean Energy Regulator under a Creative Commons Attribution 4.0
International licence.

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
