%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  omixVizR
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Omics Data Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-genpwr 
BuildRequires:    R-CRAN-ggbreak 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-lulab.utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-genpwr 
Requires:         R-CRAN-ggbreak 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-ggtext 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-lulab.utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-tibble 

%description
Provides a suite of tools for the comprehensive visualization of
multi-omics data, including genomics, transcriptomics, and proteomics.
Offers user-friendly functions to generate publication-quality plots,
thereby facilitating the exploration and interpretation of complex
biological datasets. Supports seamless integration with popular R
visualization frameworks and is well-suited for both exploratory data
analysis and the presentation of final results. Key formats and methods
are presented in Huang, S., et al. (2024) "The Born in Guangzhou Cohort
Study enables generational genetic discoveries"
<doi:10.1038/s41586-023-06988-4>.

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
