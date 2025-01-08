%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Certara.RsNLME.ModelExecutor
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Execute Pharmacometric Models Using 'shiny'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-bslib >= 0.7.0
BuildRequires:    R-CRAN-Certara.RsNLME 
BuildRequires:    R-CRAN-Certara.NLME8 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinymeta 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-bslib >= 0.7.0
Requires:         R-CRAN-Certara.RsNLME 
Requires:         R-CRAN-Certara.NLME8 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinymeta 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DT 

%description
Execute Nonlinear Mixed Effects (NLME) models for pharmacometrics using a
'shiny' interface. Specify engine parameters and select from different run
options, including simple estimation, stepwise covariate search,
bootstrapping, simulation, visual predictive check, and more. Models are
executed using the 'Certara.RsNLME' package.

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
