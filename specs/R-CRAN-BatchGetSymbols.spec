%global __brp_check_rpaths %{nil}
%global packname  BatchGetSymbols
%global packver   2.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Downloads and Organizes Financial Data for Multiple Tickers

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-crayon 

%description
Makes it easy to download financial data from Yahoo Finance
<https://finance.yahoo.com/>.

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
