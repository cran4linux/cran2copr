%global __brp_check_rpaths %{nil}
%global packname  rplos
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the Search API for 'PLoS' Journals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-solrium >= 1.0.2
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-solrium >= 1.0.2
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-whisker 

%description
A programmatic interface to the 'SOLR' based search API
(<http://api.plos.org/>) provided by the Public Library of Science
journals to search their articles. Functions are included for searching
for articles, retrieving articles, making plots, doing 'faceted' searches,
'highlight' searches, and viewing results of 'highlighted' searches in a
browser.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
