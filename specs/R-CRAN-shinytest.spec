%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinytest
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Test Shiny Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 2.0.3
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-webdriver >= 1.0.6
BuildRequires:    R-CRAN-testthat >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.8.9002
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-debugme 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rematch 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-callr >= 2.0.3
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-webdriver >= 1.0.6
Requires:         R-CRAN-testthat >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.8.9002
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-debugme 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rematch 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
For automated testing of Shiny applications, using a headless browser,
driven through 'WebDriver'.

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
