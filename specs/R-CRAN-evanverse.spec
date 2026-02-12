%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evanverse
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions for Data Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pwr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-pwr 

%description
A comprehensive collection of utility functions for data analysis and
visualization in R. The package provides 60+ functions for data
manipulation, file handling, color palette management, bioinformatics
workflows, statistical analysis, plotting, and package management.
Features include void value handling, custom infix operators, flexible
file I/O, and publication-ready visualizations with sensible defaults.
Implementation follows tidyverse principles (Wickham et al. (2019)
<doi:10.21105/joss.01686>) and incorporates best practices from the R
community.

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
