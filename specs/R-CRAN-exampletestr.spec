%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exampletestr
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Help for Writing Unit Tests Based on Function Examples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.1
BuildRequires:    R-CRAN-checkmate >= 2.0
BuildRequires:    R-CRAN-readr >= 2.0
BuildRequires:    R-CRAN-usethis >= 2.0
BuildRequires:    R-CRAN-fs >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.5
BuildRequires:    R-CRAN-strex >= 1.4.2
BuildRequires:    R-CRAN-styler >= 1.2
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-rstudioapi >= 0.4
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-roxygen2 
Requires:         R-CRAN-withr >= 2.1
Requires:         R-CRAN-checkmate >= 2.0
Requires:         R-CRAN-readr >= 2.0
Requires:         R-CRAN-usethis >= 2.0
Requires:         R-CRAN-fs >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.5
Requires:         R-CRAN-strex >= 1.4.2
Requires:         R-CRAN-styler >= 1.2
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-rstudioapi >= 0.4
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-roxygen2 

%description
Take the examples written in your documentation of functions and use them
to create shells (skeletons which must be manually completed by the user)
of test files to be tested with the 'testthat' package. Sort of like
python 'doctests' for R.

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
