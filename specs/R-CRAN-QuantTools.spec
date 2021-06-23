%global __brp_check_rpaths %{nil}
%global packname  QuantTools
%global packver   0.5.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Enhanced Quantitative Trading Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fasttime 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-fasttime 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-R6 

%description
Download and organize historical market data from multiple sources like
Yahoo (<https://finance.yahoo.com>), Google
(<https://www.google.com/finance>), Finam
(<https://www.finam.ru/profile/moex-akcii/sberbank/export/>), MOEX
(<https://www.moex.com/en/derivatives/contracts.aspx>) and IQFeed
(<https://www.iqfeed.net/symbolguide/index.cfm?symbolguide=lookup>). Code
your trading algorithms in modern C++11 with powerful event driven tick
processing API including trading costs and exchange communication latency
and transform detailed data seamlessly into R. In just few lines of code
you will be able to visualize every step of your trading model from tick
data to multi dimensional heat maps.

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
