%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contentanalysis
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scientific Content and Citation Analysis from PDF Documents

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pdftools >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-visNetwork >= 2.1.4
BuildRequires:    R-CRAN-magrittr >= 2.0.4
BuildRequires:    R-CRAN-openalexR >= 2.0.2
BuildRequires:    R-CRAN-jsonlite >= 2.0.0
BuildRequires:    R-CRAN-stringr >= 1.5.2
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.1.0
BuildRequires:    R-CRAN-tidytext >= 0.4.3
BuildRequires:    R-CRAN-httr2 >= 0.2.0
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-pdftools >= 3.6.0
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-visNetwork >= 2.1.4
Requires:         R-CRAN-magrittr >= 2.0.4
Requires:         R-CRAN-openalexR >= 2.0.2
Requires:         R-CRAN-jsonlite >= 2.0.0
Requires:         R-CRAN-stringr >= 1.5.2
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.1.0
Requires:         R-CRAN-tidytext >= 0.4.3
Requires:         R-CRAN-httr2 >= 0.2.0
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-igraph 

%description
Provides comprehensive tools for extracting and analyzing scientific
content from PDF documents, including citation extraction, reference
matching, text analysis, and bibliometric indicators. Supports
multi-column PDF layouts, 'CrossRef' API
<https://www.crossref.org/documentation/retrieve-metadata/rest-api/>
integration, and advanced citation parsing.

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
