%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PNADCperiods
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Reference Periods in Brazil's PNADC Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.9.4
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-sidrar >= 0.2.9
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.9.4
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-sidrar >= 0.2.9

%description
Identifies reference periods (months, fortnights, and weeks) in Brazil's
quarterly PNADC (Pesquisa Nacional por Amostra de Domicilios Continua)
survey data and computes calibrated weights for sub-quarterly analysis.
The core algorithm uses IBGE (Instituto Brasileiro de Geografia e
Estatistica) 'Parada Tecnica' (technical break) rules combined with
respondent birthdates to determine which temporal period each survey
observation refers to. Period identification follows a nested hierarchy
enforced by construction: fortnights require months, weeks require
fortnights. Achieves approximately 97%% monthly determination rate with the
full series (2012-2025). Strict fortnight and week rates are approximately
9%% and 3%% respectively, as they cannot leverage cross-quarter panel
aggregation. Experimental strategies (probabilistic assignment and UPA
(Primary Sampling Unit) aggregation) further improve these determination
rates. The package provides adaptive hierarchical weight calibration
(4/2/1 cell levels for month/fortnight/week) with period-specific
smoothing to produce survey weights calibrated to SIDRA (Sistema IBGE de
Recuperacao Automatica) population totals. Also includes a SIDRA
mensalization module that converts 86+ official rolling quarter series
from the IBGE SIDRA API (Application Programming Interface) into exact
monthly estimates, without requiring access to microdata. Hecksher (2020)
<https://repositorio.ipea.gov.br/handle/11058/9859>.

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
