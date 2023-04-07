%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  readtext
%global packver   0.82
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.82
Release:          1%{?dist}%{?buildtag}
Summary:          Import and Handling for Plain and Formatted Text Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-readODS >= 1.7.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.10
BuildRequires:    R-CRAN-antiword 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-streamR 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-striprtf 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
Requires:         R-CRAN-readODS >= 1.7.0
Requires:         R-CRAN-jsonlite >= 0.9.10
Requires:         R-CRAN-antiword 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-streamR 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-striprtf 
Requires:         R-CRAN-xml2 
Requires:         R-utils 

%description
Functions for importing and handling text files and formatted text files
with additional meta-data, such including '.csv', '.tab', '.json', '.xml',
'.html', '.pdf', '.doc', '.docx', '.rtf', '.xls', '.xlsx', and others.

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
