%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OlinkAnalyze
%global packver   3.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Facilitate Analysis of Proteomic Data from Olink

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstatix 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-zip 

%description
A collection of functions to facilitate analysis of proteomic data from
Olink, primarily NPX data that has been exported from Olink Software. The
functions also work on QUANT data from Olink by log- transforming the
QUANT data. The functions are focused on reading data, facilitating data
wrangling and quality control analysis, performing statistical analysis
and generating figures to visualize the results of the statistical
analysis. The goal of this package is to help users extract biological
insights from proteomic data run on the Olink platform.

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
