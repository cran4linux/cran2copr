%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  connectwidgets
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Organize and Curate Your Content Within 'Posit Connect'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-reactR 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-sass 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-reactR 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-sass 

%description
A collection of helper functions and 'htmlwidgets' to help publishers
curate content collections on 'Posit Connect'. The components, Card, Grid,
Table, Search, and Filter can be used to produce a showcase page or
gallery contained within a static or interactive R Markdown page.

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
