%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riskweightedassets
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Risk-Weighted Asset Calculations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Provides transparent, deterministic and auditable calculations of
risk-weighted assets, own-funds requirements, interest-rate risk in the
banking book and related capital metrics. It supports canonical in-memory
tables and versioned spreadsheet datasets, strict validation, synthetic
reference profiles, bitemporal snapshots, calculation controls and
traceable regulatory source metadata. Methods are parameterised against
the European Parliament and Council (2013) Capital Requirements Regulation
<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575> and
its amending Regulation (EU) 2024/1623
<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1623>. A
granular analyst API exposes individual formulae, domain views, controls,
schemas and auditable parameter overrides. The implementation is intended
for analytical, educational and model-validation use and does not
constitute legal or supervisory advice.

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
