%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  immunarch
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bioinformatics Analysis of T-Cell and B-Cell Immune Repertoires

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-UpSetR >= 1.4.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-factoextra >= 1.0.4
BuildRequires:    R-CRAN-pheatmap >= 1.0.12
BuildRequires:    R-CRAN-dtplyr >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-ggrepel >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-ggpubr >= 0.2
BuildRequires:    R-CRAN-Rtsne >= 0.15
BuildRequires:    R-CRAN-ggalluvial >= 0.10.0
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-airr 
BuildRequires:    R-CRAN-ggseqlogo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-ggraph 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-UpSetR >= 1.4.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-factoextra >= 1.0.4
Requires:         R-CRAN-pheatmap >= 1.0.12
Requires:         R-CRAN-dtplyr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-ggrepel >= 0.8.0
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-ggpubr >= 0.2
Requires:         R-CRAN-Rtsne >= 0.15
Requires:         R-CRAN-ggalluvial >= 0.10.0
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-airr 
Requires:         R-CRAN-ggseqlogo 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rlist 
Requires:         R-utils 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-ggraph 

%description
A comprehensive framework for bioinformatics exploratory analysis of bulk
and single-cell T-cell receptor and antibody repertoires. It provides
seamless data loading, analysis and visualisation for AIRR (Adaptive
Immune Receptor Repertoire) data, both bulk immunosequencing (RepSeq) and
single-cell sequencing (scRNAseq). Immunarch implements most of the widely
used AIRR analysis methods, such as: clonality analysis, estimation of
repertoire similarities in distribution of clonotypes and gene segments,
repertoire diversity analysis, annotation of clonotypes using external
immune receptor databases and clonotype tracking in vaccination and cancer
studies. A successor to our previously published 'tcR' immunoinformatics
package (Nazarov 2015) <doi:10.1186/s12859-015-0613-1>.

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
