%global __brp_check_rpaths %{nil}
%global packname  cimir
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the CIMIS Web API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-glue >= 1.3
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.3
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-glue >= 1.3
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-purrr >= 0.3

%description
Connect to the California Irrigation Management Information System (CIMIS)
Web API. See the CIMIS main page <https://cimis.water.ca.gov> and web API
documentation <https://et.water.ca.gov> for more information.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
