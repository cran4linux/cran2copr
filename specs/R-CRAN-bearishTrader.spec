%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bearishTrader
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Trading Strategies for Bearish Outlook

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
Requires:         R-graphics 

%description
Stock, Options and Futures Trading Strategies for Traders and Investors
with Bearish Outlook. The indicators, strategies, calculations, functions
and all other discussions are for academic, research, and educational
purposes only and should not be construed as investment advice and come
with absolutely no Liability. Guy Cohen (“The Bible of Options Strategies
(2nd ed.)”, 2015, ISBN: 9780133964028). Juan A. Serur, Juan A. Serur (“151
Trading Strategies”, 2018, ISBN: 9783030027919). Chartered Financial
Analyst Institute ("Chartered Financial Analyst Program Curriculum 2020
Level I Volumes 1-6. (Vol. 5, pp. 385-453)", 2019, ISBN: 9781119593577).
John C. Hull (“Options, Futures, and Other Derivatives (11th ed.)”, 2022,
ISBN: 9780136939979).

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
