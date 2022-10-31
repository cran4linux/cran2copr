%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OnboardClient
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bindings for Onboard Data's Building Data API

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-plyr >= 1.8.7
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-httr >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-rrapply >= 1.2.5
BuildRequires:    R-CRAN-tidyr >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-rstudioapi >= 0.14
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-plyr >= 1.8.7
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-httr >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-rrapply >= 1.2.5
Requires:         R-CRAN-tidyr >= 1.2.1
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-tidyselect >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-rstudioapi >= 0.14

%description
Provides a wrapper for the Onboard Data building data API
<https://api.onboarddata.io/swagger>. Along with streamlining access to
the API, this package simplifies access to sensor time series data,
metadata (sensors, equipment, and buildings), and details about the
Onboard data model/ontology.

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
