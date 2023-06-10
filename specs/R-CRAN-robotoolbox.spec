%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robotoolbox
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the 'KoboToolbox' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-labelled >= 2.11.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.7.6
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-crul >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-dm >= 1.0.5
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-RcppSimdJson >= 0.1.6
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-labelled >= 2.11.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-stringi >= 1.7.6
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-crul >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-dm >= 1.0.5
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-RcppSimdJson >= 0.1.6

%description
Suite of utilities for accessing and manipulating data from the
'KoboToolbox' API. 'KoboToolbox' is a robust platform designed for field
data collection in various disciplines. This package aims to simplify the
process of fetching and handling data from the API. Detailed documentation
for the 'KoboToolbox' API can be found at
<https://support.kobotoolbox.org/api.html>.

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
