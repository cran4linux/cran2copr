%global packname  daiR
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface with Google Cloud Document AI API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-gargle 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-googleCloudStorageR 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-gargle 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-googleCloudStorageR 
Requires:         R-grDevices 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 

%description
R interface for the Google Cloud Services 'Document AI API'
<https://cloud.google.com/document-ai/> with additional tools for output
file parsing and text reconstruction. 'Document AI' is a powerful
server-based OCR processor that extracts text and tables from images and
pdf files with high accuracy. 'daiR' gives R users programmatic access to
this processor and additional tools to handle and visualize the output.
See the package website <https://dair.info/> for more information and
examples.

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
