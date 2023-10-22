%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tfrmtbuilder
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' App Companion to the 'tfrmt' Package

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tfrmt >= 0.1.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-webshot2 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-fontawesome 
Requires:         R-CRAN-tfrmt >= 0.1.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-webshot2 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-fontawesome 

%description
Provides an interactive interface to the 'tfrmt' package. Users can
import, modify, and export tables and templates with little to no code.

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
