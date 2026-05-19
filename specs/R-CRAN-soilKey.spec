%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilKey
%global packver   0.9.97
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.97
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Soil Profile Classification per 'WRB' 2022, 'SiBCS' 5 and 'USDA' Soil Taxonomy 13

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-withr 

%description
Implements deterministic classification keys for the World Reference Base
for Soil Resources ('WRB') 2022, 4th edition (IUSS Working Group WRB,
2022, ISBN:979-8-9862451-1-9), the Brazilian System of Soil Classification
('SiBCS') 5th edition (Santos et al., 2018, ISBN:978-85-7035-800-4) and
the United States Department of Agriculture ('USDA') Soil Taxonomy 13th
edition (Soil Survey Staff, 2022,
<https://www.nrcs.usda.gov/resources/guides-and-instructions/keys-to-soil-taxonomy>).
Provides a unified profile representation with explicit per-attribute
provenance, multimodal extraction from field reports and photos via
vision-language models (VLM), spatial priors from 'SoilGrids' (Poggio et
al., 2021, <doi:10.5194/soil-7-217-2021>) and national soil maps, and
gap-filling of soil attributes from visible-near-infrared (Vis-NIR) or
mid-infrared (MIR) spectra via the Open Soil Spectral Library ('OSSL';
Safanelli et al., 2025, <doi:10.7717/peerj.18908>). The taxonomic key
itself is never delegated to a large language model (LLM); LLMs are
restricted to schema-validated extraction. Each classification result
reports a key trace, a provenance-aware evidence grade, and ambiguities
that further measurement would resolve.

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
