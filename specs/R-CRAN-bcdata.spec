%global __brp_check_rpaths %{nil}
%global packname  bcdata
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Search and Retrieve Data from the BC Data Catalogue

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-dbplyr >= 1.3.0
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-crul >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-sf >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-purrr >= 0.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-dbplyr >= 1.3.0
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-crul >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-sf >= 0.7
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-purrr >= 0.2
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-readxl 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Search, query, and download tabular and 'geospatial' data from the British
Columbia Data Catalogue (<https://catalogue.data.gov.bc.ca/>).  Search
catalogue data records based on keywords, data licence, sector, data
format, and B.C. government organization. View metadata directly in R,
download many data formats, and query 'geospatial' data available via the
B.C. government Web Feature Service ('WFS') using 'dplyr' syntax.

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
