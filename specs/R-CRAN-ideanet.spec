%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ideanet
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Data Exchange and Analysis for Networks ('ideanet')

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.1.0
BuildRequires:    R-CRAN-igraphdata 
BuildRequires:    R-CRAN-CliquePercolation 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-concorR 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-linkcomm 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-igraph >= 2.1.0
Requires:         R-CRAN-igraphdata 
Requires:         R-CRAN-CliquePercolation 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-concorR 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-grDevices 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-linkcomm 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-network 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
A suite of convenient tools for social network analysis geared toward
students, entry-level users, and non-expert practitioners. ‘ideanet’
features unique functions for the processing and measurement of
sociocentric and egocentric network data. These functions automatically
generate node- and system-level measures commonly used in the analysis of
these types of networks. Outputs from these functions maximize the ability
of novice users to employ network measurements in further analyses while
making all users less prone to common data analytic errors. Additionally,
‘ideanet’ features an R Shiny graphic user interface that allows novices
to explore network data with minimal need for coding.

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
