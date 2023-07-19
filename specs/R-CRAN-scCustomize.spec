%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scCustomize
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Custom Visualizations & Functions for Streamlined Analyses of Single Cell Sequencing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 4.3.0
BuildRequires:    R-CRAN-SeuratObject >= 4.1.2
BuildRequires:    R-CRAN-cli >= 3.2.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-rlang >= 1.0.1
BuildRequires:    R-CRAN-scattermore >= 0.7
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggprism 
BuildRequires:    R-CRAN-ggrastr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-Seurat >= 4.3.0
Requires:         R-CRAN-SeuratObject >= 4.1.2
Requires:         R-CRAN-cli >= 3.2.0
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-rlang >= 1.0.1
Requires:         R-CRAN-scattermore >= 0.7
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggprism 
Requires:         R-CRAN-ggrastr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Collection of functions created and/or curated to aid in the visualization
and analysis of single-cell data using 'R'.  'scCustomize' aims to provide
1) Customized visualizations for aid in ease of use and to create more
aesthetic and functional visuals. 2) Improve speed/reproducibility of
common tasks/pieces of code in scRNA-seq analysis with a single or group
of functions.  For citation please use: Marsh SE (2021) "Custom
Visualizations & Functions for Streamlined Analyses of Single Cell
Sequencing" <doi:10.5281/zenodo.5706430>.

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
