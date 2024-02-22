%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BRVM
%global packver   5.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve Historical Data of Companies Listed on the 'BRVM' Stock Exchange

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gsheet 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gsheet 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-lubridate 

%description
Provide real-time access to data from the Regional Securities Exchange
SA(<https://www.brvm.org/en>), commonly known as the 'BRVM' stock
exchange. The goal is to facilitate data access for users of the R
programming language. The package includes a variety of data that can be
accessed by calling functions.

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
