%global __brp_check_rpaths %{nil}
%global packname  excluder
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Checks for Exclusion Criteria in Online Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-iptools 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-iptools 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Data that are collected through online sources such as Mechanical Turk may
require excluding rows because of IP address duplication, geolocation, or
completion duration. This package facilitates exclusion of these data for
Qualtrics datasets.

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
