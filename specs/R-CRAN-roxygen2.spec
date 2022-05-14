%global __brp_check_rpaths %{nil}
%global packname  roxygen2
%global packver   7.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          In-Line Documentation for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-pkgload >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-pkgload >= 1.0.2
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-brew 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xml2 

%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field
using specially formatted comments. Writing documentation in-line with
code makes it easier to keep your documentation up-to-date as your
requirements change. 'Roxygen2' is inspired by the 'Doxygen' system for
C++.

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
