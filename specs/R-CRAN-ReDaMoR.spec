%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ReDaMoR
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Relational Data Modeler

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 

%description
The aim of this package is to manipulate relational data models in R. It
provides functions to create, modify and export data models in json
format. It also allows importing models created with 'MySQL Workbench'
(<https://www.mysql.com/products/workbench/>). These functions are
accessible through a graphical user interface made with 'shiny'.
Constraints such as types, keys, uniqueness and mandatory fields are
automatically checked and corrected when editing a model. Finally, real
data can be confronted to a model to check their compatibility.

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
