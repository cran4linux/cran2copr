%global packname  immunarch
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          2%{?dist}
Summary:          Bioinformatics Analysis of T-Cell and B-Cell Immune Repertoires

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-gridExtra >= 2.2
BuildRequires:    R-CRAN-tibble >= 2.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-UpSetR >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dbplyr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
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
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-airr 
BuildRequires:    R-CRAN-ggseqlogo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plyr 
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-gridExtra >= 2.2
Requires:         R-CRAN-tibble >= 2.0
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-UpSetR >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dbplyr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
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
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-airr 
Requires:         R-CRAN-ggseqlogo 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plyr 

%description
A comprehensive framework for bioinformatics analysis of bulk and
single-cell T-cell receptor and antibody repertoires. It provides seamless
data loading, analysis and visualisation for AIRR (Adaptive Immune
Receptor Repertoire) data, both bulk immunosequencing (RepSeq) and
single-cell sequencing (scRNAseq). It implements most of the widely used
AIRR analysis methods, such as: clonality analysis, estimation of
repertoire similarities in distribution of clonotypes and gene segments,
repertoire diversity analysis, annotation of clonotypes using external
immune receptor databases and clonotype tracking in vaccination and cancer
studies. A successor to our previously published 'tcR' immunoinformatics
package (Nazarov 2015) <doi:10.1186/s12859-015-0613-1>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
