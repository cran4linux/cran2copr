%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pctax
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Professional Comprehensive Omics Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-pcutils >= 0.2.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-pcutils >= 0.2.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-magrittr 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-scales 

%description
Provides a comprehensive suite of tools for analyzing omics data. It
includes functionalities for alpha diversity analysis, beta diversity
analysis, differential abundance analysis, community assembly analysis,
visualization of phylogenetic tree, and functional enrichment analysis.
With a progressive approach, the package offers a range of analysis
methods to explore and understand the complex communities. It is designed
to support researchers and practitioners in conducting in-depth and
professional omics data analysis.

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
