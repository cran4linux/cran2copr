%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mergenstudio
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Mergen' Studio: An 'RStudio' Addin Wrapper for the 'Mergen' Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-bslib >= 0.4.2
BuildRequires:    R-CRAN-rstudioapi >= 0.12
BuildRequires:    R-CRAN-mergen 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-ids 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shiny.i18n 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-methods 
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-bslib >= 0.4.2
Requires:         R-CRAN-rstudioapi >= 0.12
Requires:         R-CRAN-mergen 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-ids 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shiny.i18n 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rvest 
Requires:         R-utils 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rmarkdown 
Requires:         R-methods 

%description
An 'RStudio' Addin wrapper for the 'mergen' package. This package employs
artificial intelligence to convert data analysis questions into executable
code, explanations, and algorithms. This package makes it easier to use
Large Language Models in your development environment by providing a
chat-like interface, while also allowing you to inspect and execute the
returned code.

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
