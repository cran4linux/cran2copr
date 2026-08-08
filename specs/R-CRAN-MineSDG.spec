%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MineSDG
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mining Industry SDG Impact Calculator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Provides tools to calculate quantitative scores for the United Nations
Sustainable Development Goals (SDGs) for the mining, minerals and metals
sector. Retrieves official indicator data from the 'United Nations SDG
API', runs trend, stability, benchmarking and convergence diagnostics,
maps indicators to mining-sector materiality domains via a bundled
ontology, computes site-level Key Performance Indicators (KPIs) aligned
with Global Reporting Initiative (GRI) 11, International Council on Mining
and Metals (ICMM) Mining Principles and Sustainability Accounting
Standards Board (SASB) EM-MM conventions, scores sites on a 0-100 SDG
scorecard, and ships an interactive 'shiny' dashboard with demonstration
datasets. An Environmental, Social and Governance (ESG) reporting layer
generates Global Reporting Initiative (GRI), International Council on
Mining and Metals (ICMM) and Business Responsibility and Sustainability
Reporting (BRSR) reports from a disclosure bundle interface, with
framework mappings shipped as data and rendering to 'HTML', 'PDF', 'Word'
and 'Excel' via 'Quarto' and 'openxlsx2'. Official Sustainable Development
Goals information and indicator methodology are available from the United
Nations Sustainable Development Goals website <https://sdgs.un.org/goals>.

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
