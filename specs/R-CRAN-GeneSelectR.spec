%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeneSelectR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'GeneSelectR' - Comprehensive Feature Selection Workflow for Bulk RNAseq Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.2.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-reticulate >= 1.28
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tmod >= 0.50.13
Requires:         R-methods >= 4.2.2
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-reticulate >= 1.28
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tmod >= 0.50.13

%description
The workflow is a versatile R package designed for comprehensive feature
selection in bulk RNAseq datasets. Its key innovation lies in the seamless
integration of the 'Python' 'scikit-learn'
(<https://scikit-learn.org/stable/index.html>) machine learning framework
with R-based bioinformatics tools. 'GeneSelectR' performs robust Machine
Learning-driven (ML) feature selection while leveraging 'Gene Ontology'
(GO) enrichment analysis as described by Thomas PD et al. (2022)
<doi:10.1002/pro.4218>, using 'clusterProfiler' (Wu et al., 2021)
<doi:10.1016/j.xinn.2021.100141> and semantic similarity analysis powered
by 'simplifyEnrichment' (Gu, Huebschmann, 2021)
<doi:10.1016/j.gpb.2022.04.008>. This combination of methodologies
optimizes computational and biological insights for analyzing complex
RNAseq datasets.

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
