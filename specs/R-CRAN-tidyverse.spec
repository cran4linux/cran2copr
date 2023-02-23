%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyverse
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'Tidyverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.1
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-haven >= 2.5.1
BuildRequires:    R-CRAN-dbplyr >= 2.3.0
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-reprex >= 2.0.2
BuildRequires:    R-CRAN-googledrive >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.4
BuildRequires:    R-CRAN-pillar >= 1.8.1
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-httr >= 1.4.4
BuildRequires:    R-CRAN-readxl >= 1.4.2
BuildRequires:    R-CRAN-xml2 >= 1.3.3
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-ragg >= 1.2.5
BuildRequires:    R-CRAN-dtplyr >= 1.2.2
BuildRequires:    R-CRAN-conflicted >= 1.2.0
BuildRequires:    R-CRAN-hms >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-broom >= 1.0.3
BuildRequires:    R-CRAN-rvest >= 1.0.3
BuildRequires:    R-CRAN-googlesheets4 >= 1.0.1
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.14
BuildRequires:    R-CRAN-modelr >= 0.1.10
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.1
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-haven >= 2.5.1
Requires:         R-CRAN-dbplyr >= 2.3.0
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-reprex >= 2.0.2
Requires:         R-CRAN-googledrive >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-jsonlite >= 1.8.4
Requires:         R-CRAN-pillar >= 1.8.1
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-httr >= 1.4.4
Requires:         R-CRAN-readxl >= 1.4.2
Requires:         R-CRAN-xml2 >= 1.3.3
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-ragg >= 1.2.5
Requires:         R-CRAN-dtplyr >= 1.2.2
Requires:         R-CRAN-conflicted >= 1.2.0
Requires:         R-CRAN-hms >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-broom >= 1.0.3
Requires:         R-CRAN-rvest >= 1.0.3
Requires:         R-CRAN-googlesheets4 >= 1.0.1
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.14
Requires:         R-CRAN-modelr >= 0.1.10

%description
The 'tidyverse' is a set of packages that work in harmony because they
share common data representations and 'API' design. This package is
designed to make it easy to install and load multiple 'tidyverse' packages
in a single step. Learn more about the 'tidyverse' at
<https://www.tidyverse.org>.

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
