%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.reporter
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reporting Tools for 'shiny' Modules

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.23
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-gtsummary >= 2.0.0
BuildRequires:    R-CRAN-commonmark >= 1.9.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.9
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-knitr >= 1.42
BuildRequires:    R-CRAN-yaml >= 1.1.0
BuildRequires:    R-CRAN-zip >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-flextable >= 0.9.2
BuildRequires:    R-CRAN-bslib >= 0.8.0
BuildRequires:    R-CRAN-teal.data >= 0.8.0
BuildRequires:    R-CRAN-teal.code >= 0.7.0
BuildRequires:    R-CRAN-rtables >= 0.6.11
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-sortable >= 0.5.0
BuildRequires:    R-CRAN-shinybusy >= 0.3.2
BuildRequires:    R-CRAN-rlistings >= 0.2.10
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-rtables.officer >= 0.0.2
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-rmarkdown >= 2.23
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-gtsummary >= 2.0.0
Requires:         R-CRAN-commonmark >= 1.9.2
Requires:         R-CRAN-jsonlite >= 1.8.9
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-knitr >= 1.42
Requires:         R-CRAN-yaml >= 1.1.0
Requires:         R-CRAN-zip >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-flextable >= 0.9.2
Requires:         R-CRAN-bslib >= 0.8.0
Requires:         R-CRAN-teal.data >= 0.8.0
Requires:         R-CRAN-teal.code >= 0.7.0
Requires:         R-CRAN-rtables >= 0.6.11
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-sortable >= 0.5.0
Requires:         R-CRAN-shinybusy >= 0.3.2
Requires:         R-CRAN-rlistings >= 0.2.10
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-rtables.officer >= 0.0.2
Requires:         R-CRAN-bsicons 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-tools 
Requires:         R-utils 

%description
Prebuilt 'shiny' modules containing tools for the generation of
'rmarkdown' reports, supporting reproducible research and analysis.

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
