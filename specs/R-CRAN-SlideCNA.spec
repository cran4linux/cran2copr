%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SlideCNA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calls Copy Number Alterations from Slide-Seq Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-mltools 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-mltools 
Requires:         R-utils 

%description
This takes spatial single-cell-type RNA-seq data (specifically designed
for Slide-seq v2) that calls copy number alterations (CNAs) using
pseudo-spatial binning, clusters cellular units (e.g. beads) based on CNA
profile, and visualizes spatial CNA patterns. Documentation about
'SlideCNA' is included in the the pre-print by Zhang et al. (2022,
<doi:10.1101/2022.11.25.517982>). The package 'enrichR' (>= 3.0),
conditionally used to annotate SlideCNA-determined clusters with gene
ontology terms, can be installed at <https://github.com/wjawaid/enrichR>
or with install_github("wjawaid/enrichR").

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
