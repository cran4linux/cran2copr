%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurveySolutionsAPIv2
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive API Access to Your 'Survey Solutions' Server Using 'httr2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-susographql >= 0.1.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyjson 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-susographql >= 0.1.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyjson 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-zip 

%description
A comprehensive suite of functions for interfacing with the 'Survey
Solutions' APIs (<https://demo.mysurvey.solutions/apidocs/index.html> and
<https://docs.mysurvey.solutions/>). It supports all the current POST,
GET, and PATCH requests of the 'REST' API and extends its capabilities by
integrating selected 'GraphQL' API queries and mutations when 'REST' API
equivalents are not available. Designed for ease of use, it includes
several convenience functions to streamline operations. The package
ensures that data retrieved from the API is automatically transformed into
a single, easy-to-use data frame or data table, optimizing it for
subsequent analysis and processing. Additionally, it is specifically
designed to facilitate seamless integration into 'shiny' applications,
enhancing the interactive web application development experience. Built on
the robust 'httr2' package, this version supersedes the previous
'httr'-based implementation. Recognizing the needs of large-scale data
operations such as censuses, the package also incorporates features for
parallel processing, enhancing its efficiency and scalability.

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
