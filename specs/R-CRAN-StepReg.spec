%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StepReg
%global packver   1.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Regression Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 

%description
Stepwise regression is a statistical technique used for model selection.
This package streamlines stepwise regression analysis by supporting
multiple regression types, incorporating popular selection strategies, and
offering essential metrics. It enables users to apply multiple selection
strategies and metrics in a single function call, visualize variable
selection processes, and export results in various formats. However,
StepReg should not be used for statistical inference unless the variable
selection process is explicitly accounted for, as it can compromise the
validity of the results. This limitation does not apply when StepReg is
used for prediction purposes. We validated StepReg's accuracy using public
datasets within the SAS software environment. Additionally, StepReg
features an interactive Shiny application to enhance usability and
accessibility.

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
