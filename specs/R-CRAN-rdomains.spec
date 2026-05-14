%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdomains
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Get the Category of Content Hosted by a Domain

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
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
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-virustotal 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-checkmate >= 2.3.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-virustotal 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R.utils 

%description
Get the category of content hosted by a domain. Use Shallalist (service
discontinued), 'VirusTotal' (which provides access to lots of services)
<https://www.virustotal.com/>, 'DMOZ'
<https://archive.org/details/dmoz-rdf-20150327>, University Domain list
<https://github.com/Hipo/university-domains-list>, 'OpenAI' 'GPT' models,
'Anthropic' 'Claude' models, or validated machine learning classifiers
based on 'Shallalist' data to learn about the kind of content hosted by a
domain.

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
