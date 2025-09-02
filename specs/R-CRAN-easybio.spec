%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easybio
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Single-Cell Annotation and Transcriptomic Analysis Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-xml2 

%description
Provides a comprehensive toolkit for single-cell annotation with the
'CellMarker2.0' database (see Xia Li, Peng Wang, Yunpeng Zhang (2023)
<doi: 10.1093/nar/gkac947>). Streamlines biological label assignment in
single-cell RNA-seq data and facilitates transcriptomic analysis,
including preparation of TCGA<https://portal.gdc.cancer.gov/> and
GEO<https://www.ncbi.nlm.nih.gov/geo/> datasets, differential expression
analysis and visualization of enrichment analysis results. Additional
utility functions support various bioinformatics workflows. See Wei Cui
(2024) <doi: 10.1101/2024.09.14.609619> for more details.

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
