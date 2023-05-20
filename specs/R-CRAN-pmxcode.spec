%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pmxcode
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Pharmacometric Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-golem >= 0.3.3
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-golem >= 0.3.3
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinyFiles 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xfun 

%description
Provides a user interface to create or modify pharmacometric models for
various modeling and simulation software platforms.

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
