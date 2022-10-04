%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  margaret
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Scientometric Analysis Minciencias

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-scholar 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-treemapify 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-widyr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-scholar 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-treemapify 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-widyr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-igraph 

%description
The target of 'margaret' is help to extract data from Minciencias to
analyze scientific production in Colombia.

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
