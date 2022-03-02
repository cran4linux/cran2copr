%global __brp_check_rpaths %{nil}
%global packname  salesforcer
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of 'Salesforce' APIs Using Tidy Principles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-XML >= 3.99.0.3
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-utils >= 3.6.0
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-zip >= 2.0.4
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-mime >= 0.9
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-rlist >= 0.4.6.1
BuildRequires:    R-CRAN-anytime >= 0.3.9
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-vctrs >= 0.3.4
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-XML >= 3.99.0.3
Requires:         R-methods >= 3.6.0
Requires:         R-utils >= 3.6.0
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-zip >= 2.0.4
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-mime >= 0.9
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-rlist >= 0.4.6.1
Requires:         R-CRAN-anytime >= 0.3.9
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-vctrs >= 0.3.4
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-base64enc >= 0.1.3

%description
Functions connecting to the 'Salesforce' Platform APIs (REST, SOAP, Bulk
1.0, Bulk 2.0, Metadata, Reports and Dashboards)
<https://trailhead.salesforce.com/en/content/learn/modules/api_basics/api_basics_overview>.
"API" is an acronym for "application programming interface". Most all
calls from these APIs are supported as they use CSV, XML or JSON data that
can be parsed into R data structures. For more details please see the
'Salesforce' API documentation and this package's website
<https://stevenmmortimer.github.io/salesforcer/> for more information,
documentation, and examples.

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
