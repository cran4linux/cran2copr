%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fabR
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Functions Collection Used in Data Pipelines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-lifecycle 

%description
The goal of this package is to provide wrapper functions in the data
cleaning and cleansing processes. These function helps in messages and
interaction with the user, keep track of information in pipelines, help in
the wrangling, munging, assessment and visualization of data frame-like
material.

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
