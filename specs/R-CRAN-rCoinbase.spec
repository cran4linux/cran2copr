%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rCoinbase
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Coinbase Advance Trade API Interface'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 

%description
The 'Coinbase Advanced Trade API'
<https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/introduction>
lets you manage orders, portfolios, products, and fees with the new v3
endpoints.

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
