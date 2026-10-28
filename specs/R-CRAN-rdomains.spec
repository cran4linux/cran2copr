%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdomains
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Get the Category of Content Hosted by a Domain

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-checkmate >= 2.3.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-virustotal >= 0.7.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-spiderbar 
BuildRequires:    R-CRAN-ipaddress 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-checkmate >= 2.3.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-virustotal >= 0.7.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-spiderbar 
Requires:         R-CRAN-ipaddress 
Requires:         R-CRAN-withr 

%description
Fetch website content and classify it through the Python 'piedomains' text
model. Look up domains in UT-Capitole, Steven Black, university, archived
'Shallalist' and 'DMOZ' lists, or use 'VirusTotal'
<https://www.virustotal.com/>, 'OpenAI' and 'Anthropic' APIs. Report
collection outcomes and source provenance. Includes a historical
domain-name classifier trained on 'Shallalist' data.

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
