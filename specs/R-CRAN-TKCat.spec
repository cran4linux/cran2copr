%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TKCat
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tailored Knowledge Catalog

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonvalidate >= 1.3.2
BuildRequires:    R-CRAN-ReDaMoR >= 0.7.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ClickHouseHTTP 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-roxygen2 
Requires:         R-CRAN-jsonvalidate >= 1.3.2
Requires:         R-CRAN-ReDaMoR >= 0.7.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ClickHouseHTTP 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-future 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-roxygen2 

%description
Facilitate the management of data from knowledge resources that are
frequently used alone or together in research environments. In 'TKCat',
knowledge resources are manipulated as modeled database (MDB) objects.
These objects provide access to the data tables along with a general
description of the resource and a detail data model documenting the
tables, their fields and their relationships. These MDBs are then gathered
in catalogs that can be easily explored an shared. Finally, 'TKCat'
provides tools to easily subset, filter and combine MDBs and create new
catalogs suited for specific needs.

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
