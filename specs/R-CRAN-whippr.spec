%global __brp_check_rpaths %{nil}
%global packname  whippr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Manipulating Gas Exchange Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-patchwork >= 1.0.1
BuildRequires:    R-CRAN-broom >= 0.7.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-nlstools 
BuildRequires:    R-CRAN-pillar 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-patchwork >= 1.0.1
Requires:         R-CRAN-broom >= 0.7.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-nlstools 
Requires:         R-CRAN-pillar 

%description
Set of tools for manipulating gas exchange data from cardiopulmonary
exercise testing.

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
