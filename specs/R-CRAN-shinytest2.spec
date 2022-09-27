%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinytest2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Testing for Shiny Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-testthat >= 3.1.2
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-globals >= 0.14.0
BuildRequires:    R-CRAN-chromote >= 0.1.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-testthat >= 3.1.2
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-globals >= 0.14.0
Requires:         R-CRAN-chromote >= 0.1.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-withr 

%description
Automated unit testing of Shiny applications through a headless 'Chromium'
browser.

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
