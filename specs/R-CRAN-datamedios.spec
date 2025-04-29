%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datamedios
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scraping Chilean Media

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-wordcloud2 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-wordcloud2 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 

%description
A system for extracting news from Chilean media, specifically through Web
Scapping from Chilean media. The package allows for news searches using
search phrases and date filters, and returns the results in a structured
format, ready for analysis. Additionally, it includes functions to clean
the extracted data, visualize it, and store it in databases. All of this
can be done automatically, facilitating the collection and analysis of
relevant information from Chilean media.

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
