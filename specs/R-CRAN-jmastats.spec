%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jmastats
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Weather Data from Japan Meteorological Agency Website

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.6.3
BuildRequires:    R-CRAN-units >= 0.5.1
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.3
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-sf >= 0.6.3
Requires:         R-CRAN-units >= 0.5.1
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-rappdirs >= 0.3.3
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-rlang >= 0.2.1

%description
Provides features that allow users to download weather data published by
the Japan Meteorological Agency (JMA) website
(<https://www.jma.go.jp/jma/index.html>). The data includes information
dating back to 1976 and aligns with the categories available on the
website. Additionally, users can process the best track data of typhoons
and easily handle earthquake record files.

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
