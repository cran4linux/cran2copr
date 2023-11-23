%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WhatsR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parsing, Anonymizing and Visualizing Exported 'WhatsApp' Chat Logs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-mgsub 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qdap 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-mgsub 
Requires:         R-stats 
Requires:         R-CRAN-qdap 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 

%description
Imports 'WhatsApp' chat logs and parses them into a usable dataframe
object. The parser works on chats exported from Android or iOS phones and
on Linux, macOS and Windows. The parser has multiple options for
extracting smileys and emojis from the messages, extracting URLs and
domains from the messages, extracting names and types of sent media files
from the messages, extracting timestamps from messages, extracting and
anonymizing author names from messages. Can be used to create anonymized
versions of data.

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
