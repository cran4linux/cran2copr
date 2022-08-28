%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yfR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Downloads and Organizes Financial Data from Yahoo Finance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantmod >= 0.4.20
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-humanize 
BuildRequires:    R-methods 
Requires:         R-CRAN-quantmod >= 0.4.20
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-humanize 
Requires:         R-methods 

%description
Facilitates download of financial data from Yahoo Finance
<https://finance.yahoo.com/>, a vast repository of stock price data across
multiple financial exchanges. The package offers a local caching system
and support for parallel computation.

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
