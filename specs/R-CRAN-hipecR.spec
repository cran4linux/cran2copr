%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hipecR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analysing HIPEC Patient Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-dlookr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-webshot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-dlookr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-webshot2 

%description
Provides helper functions for analysing patient data in hyperthermic
intraperitoneal chemotherapy (HIPEC) workflows. Includes functions to
estimate peritoneal surface area (PSA), summarise registry data, and
produce reporting graphics. Body surface area calculations are based on Du
Bois and Du Bois (1916) <doi:10.1001/archinte.1916.00080130010002>.

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
