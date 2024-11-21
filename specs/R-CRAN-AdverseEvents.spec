%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AdverseEvents
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Application for Adverse Event Analysis of 'OnCore' Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-skimr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-lubridate 

%description
An application for analysis of Adverse Events, as described in Chen, et
al., (2023) <doi:10.3390/cancers15092521>. The required data for the
application includes demographics, follow up, adverse event, drug
administration and optional tumor measurement data. The app can produce
swimmers plots of adverse events, Kaplan-Meier plots and Cox Proportional
Hazards model results for the association of adverse event biomarkers and
overall survival and progression free survival. The adverse event
biomarkers include occurrence of grade 3, low grade (1-2), and treatment
related adverse events. Plots and tables of results are downloadable.

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
