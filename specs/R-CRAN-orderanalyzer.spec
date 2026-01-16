%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orderanalyzer
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extracting Order Position Tables from PDF-Based Order Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-lubridate 

%description
Functions for extracting text and tables from PDF-based order documents.
It provides an n-gram-based approach for identifying the language of an
order document. It furthermore uses R-package 'pdftools' to extract the
text from an order document. In the case that the PDF document is only
including an image (because it is scanned document), R package 'tesseract'
is used for OCR. Furthermore, the package provides functionality for
identifying and extracting order position tables in order documents based
on a clustering approach.

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
