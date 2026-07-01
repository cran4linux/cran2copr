%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilKey
%global packver   0.9.157
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.157
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Soil Profile Classification per WRB 2022, 'SiBCS' 5 and USDA Soil Taxonomy 13

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
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 

%description
Implements deterministic classification keys for the World Reference Base
for Soil Resources 2022 (4th edition) and the Brazilian System of Soil
Classification ('SiBCS', 5th edition). Provides a unified profile
representation with explicit per-attribute provenance, multimodal
extraction from field reports and photos via vision-language models,
spatial priors from 'SoilGrids' and national soil maps, and gap-filling of
soil attributes from Vis-NIR or MIR spectra via the Open Soil Spectral
Library ('OSSL'). The taxonomic key itself is never delegated to a
language model; LLMs are restricted to schema-validated extraction. Each
classification result reports a key trace, a provenance-aware evidence
grade, and ambiguities that further measurement would resolve.

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
