%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orisma
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Occupational Risk Integrated Systematic Mapping and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-pheatmap >= 1.0.12
BuildRequires:    R-CRAN-stringdist >= 0.9.8
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-CRAN-digest >= 0.6.29
BuildRequires:    R-CRAN-synthesisr >= 0.3.0
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-pheatmap >= 1.0.12
Requires:         R-CRAN-stringdist >= 0.9.8
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-CRAN-digest >= 0.6.29
Requires:         R-CRAN-synthesisr >= 0.3.0
Requires:         R-tools 
Requires:         R-utils 

%description
A complete pipeline for systematic bibliometric mapping of occupational
health and safety (OHS) evidence. Starting from reference files exported
from major bibliographic databases such as Web of Science, Scopus, PubMed,
Dimensions, EBSCO, and others, 'orisma' automates ingestion,
deduplication, relevance filtering, occupational risk category extraction,
bibliometric analysis, and report generation. The package is related to
bibliometric science mapping and evidence synthesis workflows described by
Aria and Cuccurullo (2017) <doi:10.1016/j.joi.2017.08.007>, Westgate
(2019) <doi:10.1002/jrsm.1374>, and Lajeunesse (2016)
<doi:10.1111/2041-210X.12472>, but adds a domain-specific occupational
safety and health layer. The package implements three original
bibliometric indicators: (1) the Worker-Risk Disconnection Index (WRDI),
measuring the proportion of studies that characterise an occupational risk
without including direct worker exposure data; (2) the Risk Category
Saturation Index (RCS), measuring the relative over- or
under-representation of each risk category relative to a uniform baseline;
and (3) the Material-Gap Profile (MGP), measuring the ratio between a
material's known hazard potential and its coverage in the occupational
health literature. Two additional preventive intelligence indicators are
provided: (4) the Abstract Sufficiency Score (ASS, 0-5), a cumulative
hierarchical index of the preventively useful information contained in an
abstract; and (5) the Bridge Article Score (0-5), identifying studies that
simultaneously address technology, hazardous agent, worker population,
exposure measurement, and preventive recommendations. Risk categories are
extracted using a built-in occupational risk dictionary of 58 categories
anchored in ISO 45001:2018, INSST, NIOSH, and EU-OSHA frameworks,
organised in six blocks: Safety, Industrial Hygiene, Ergonomics,
Psychosociology, Biological Hazards, and Emerging Technologies. The
dictionary is user-extensible. Outputs include bilingual HTML reports,
occupational risk sheets, priority reading rankings, guided extraction
matrices for systematic review, and reproducibility certificates with MD5
hashes.

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
