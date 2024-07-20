%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rqti
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Tests According to QTI 2.1 Standard

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-textutils 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-textutils 

%description
Create tests and tasks compliant with the Question & Test Interoperability
(QTI) information model version 2.1. Input sources are Rmd/md description
files or S4-class objects. Output formats include standalone zip or xml
files. Supports the generation of basic task types (single and multiple
choice, order, pair association, matching tables, filling gaps and essay)
and provides a comprehensive set of attributes for customizing tests.

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
