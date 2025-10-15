%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  immunarch
%global packver   0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Modal Immune Repertoire Analytics for Immunotherapy and Vaccine Design in R

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-duckplyr >= 1.1.2
BuildRequires:    R-CRAN-pheatmap >= 1.0.12
BuildRequires:    R-CRAN-dtplyr >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-immundata >= 0.0.5
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-airr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggsci 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-duckplyr >= 1.1.2
Requires:         R-CRAN-pheatmap >= 1.0.12
Requires:         R-CRAN-dtplyr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-immundata >= 0.0.5
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-airr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rlist 
Requires:         R-utils 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggsci 

%description
A comprehensive analytics framework for building reproducible pipelines on
T-cell and B-cell immune receptor repertoire data. Delivers multi-modal
immune profiling (bulk, single-cell, CITE-seq/AbSeq, spatial,
immunogenicity data), feature engineering (ML-ready feature tables and
matrices), and biomarker discovery workflows (cohort comparisons,
longitudinal tracking, repertoire similarity, enrichment). Provides a
user-friendly interface to widely used AIRR methods — clonality/diversity,
V(D)J usage, similarity, annotation, tracking, and many more. Think Scanpy
or Seurat, but for AIRR data, a.k.a. Adaptive Immune Receptor Repertoire,
VDJ-seq, RepSeq, or VDJ sequencing data. A successor to our previously
published "tcR" R package (Nazarov 2015).

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
