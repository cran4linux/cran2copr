%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  googlesheets4
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Google Sheets using the Sheets API V4

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-googledrive >= 2.1.0
BuildRequires:    R-CRAN-gargle >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-vctrs >= 0.2.3
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ids 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-googledrive >= 2.1.0
Requires:         R-CRAN-gargle >= 1.3.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-vctrs >= 0.2.3
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ids 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rematch2 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Interact with Google Sheets through the Sheets API v4
<https://developers.google.com/sheets/api>. "API" is an acronym for
"application programming interface"; the Sheets API allows users to
interact with Google Sheets programmatically, instead of via a web
browser. The "v4" refers to the fact that the Sheets API is currently at
version 4. This package can read and write both the metadata and the cell
data in a Sheet.

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
