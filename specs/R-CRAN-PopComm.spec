%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PopComm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population-Level Cell-Cell Communication Analysis Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-igraph >= 2.0.0
BuildRequires:    R-CRAN-pbmcapply >= 1.5.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Matrix >= 1.2.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-pheatmap >= 1.0.12
BuildRequires:    R-CRAN-broom >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-ggpubr >= 0.6.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Seurat >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-igraph >= 2.0.0
Requires:         R-CRAN-pbmcapply >= 1.5.0
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Matrix >= 1.2.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-pheatmap >= 1.0.12
Requires:         R-CRAN-broom >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-ggpubr >= 0.6.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-parallel 
Requires:         R-grDevices 

%description
Facilitates population-level analysis of ligand-receptor (LR) interactions
using large-scale single-cell transcriptomic data. Identifies significant
LR pairs and quantifies their interactions through correlation-based
filtering and projection score computations. Designed for large-sample
single-cell studies, the package employs statistical modeling, including
linear regression, to investigate LR relationships between cell types. It
provides a systematic framework for understanding cell-cell communication,
uncovering regulatory interactions and signaling mechanisms. Offers tools
for LR pair-level, sample-level, and differential interaction analyses,
with comprehensive visualization support to aid biological interpretation.
The methodology is described in a manuscript currently under review and
will be referenced here once published or publicly available.

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
