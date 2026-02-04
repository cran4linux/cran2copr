%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyhydat
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract and Tidy Canadian 'Hydrometric' Data

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dbplyr >= 1.1.0
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.1
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dbplyr >= 1.1.0
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.1
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-rlang >= 0.1.2

%description
Provides functions to access historical and real-time national
'hydrometric' data from Water Survey of Canada data sources and then
applies tidy data principles.

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
