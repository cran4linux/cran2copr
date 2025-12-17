%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  omicsTools
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Omics Data Process Toolbox

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.2
BuildRequires:    R-CRAN-golem >= 0.3.5
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-ggvenn 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-tools 
Requires:         R-CRAN-shiny >= 1.7.2
Requires:         R-CRAN-golem >= 0.3.5
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-ggvenn 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-viridis 
Requires:         R-tools 

%description
Processing and analyzing omics data from genomics, transcriptomics,
proteomics, and metabolomics platforms. It provides functions for
preprocessing, normalization, visualization, and statistical analysis, as
well as machine learning algorithms for predictive modeling. 'omicsTools'
is an essential tool for researchers working with high-throughput omics
data in fields such as biology, bioinformatics, and medicine.The QC-RLSC
(quality control–based robust LOESS signal correction) algorithm is used
for normalization. Dunn et al. (2011) <doi:10.1038/nprot.2011.335>.

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
