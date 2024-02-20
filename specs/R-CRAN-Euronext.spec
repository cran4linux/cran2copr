%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Euronext
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve Historical Data of Companies Listed on the 'Euronext' Stock Exchange

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-highcharter 
Requires:         R-grDevices 

%description
Provides seamless access to historical data of companies listed on the
'Euronext' Stock Exchange (<https://live.euronext.com/en>), enabling users
to retrieve real-time information directly within the R environment. With
functions tailored for data retrieval and manipulation, users can
effortlessly access a wide range of financial data, including stock
prices, trading volumes, and more. Leveraging the power of R, this package
facilitates efficient analysis and visualization of stock market trends,
aiding investors, analysts, and researchers in making informed decisions.
By combining ease of use with comprehensive data access, 'Euronext'
empowers R users to delve deep into the dynamics of European financial
markets, offering valuable insights for various financial applications.

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
