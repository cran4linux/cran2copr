%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jsmodule
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'RStudio' Addins and 'Shiny' Modules for Medical Research

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MatchIt >= 3.0.0
BuildRequires:    R-CRAN-jstable >= 1.3.8
BuildRequires:    R-CRAN-jskm >= 0.4.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-epiDisplay 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-forestploter 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-maxstat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rvg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-see 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinycustomloader 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-survIDINRI 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-MatchIt >= 3.0.0
Requires:         R-CRAN-jstable >= 1.3.8
Requires:         R-CRAN-jskm >= 0.4.4
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-epiDisplay 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-forestploter 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-maxstat 
Requires:         R-methods 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rvg 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-see 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-survIDINRI 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-timeROC 
Requires:         R-utils 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-gridExtra 

%description
'RStudio' addins and 'Shiny' modules for descriptive statistics,
regression and survival analysis.

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
