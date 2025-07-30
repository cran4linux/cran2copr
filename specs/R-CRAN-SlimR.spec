%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SlimR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Marker-Based Package for Single-Cell and Spatial-Transcriptomic Annotation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 

%description
Annotating single-cell and spatial-transcriptomic (ST) data based on the
Marker dataset. It supports the creation of a unified marker list,
Markers_list, using sources including: the package's built-in curated
species-specific cell type and marker reference databases (e.g.,
'Cellmarker2', 'PanglaoDB'), Seurat objects containing cell label
information, or user-provided Excel tables mapping cell types to markers.
Based on the Markers_list, 'SlimR' can iterate through different cell
types to generate corresponding annotation reference plots (e.g.,
'Markers_Dotplot', 'Metric_Heatmap', 'Mean_expression_Box_plot').
Furthermore, it enables one-click generation of an annotation heatmap
('Annotation_Heatmap') visualizing the relationship between input cell
types and the reference marker list. For more details see Kabacoff (2015,
ISBN:9781617291388) and Hu et al. (2023) <doi:10.1093/nar/gkac947> and
Franzén et al. (2019) <doi:10.1093/database/baz046>.

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
