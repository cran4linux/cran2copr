%global __brp_check_rpaths %{nil}
%global packname  ugatsdb
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Uganda Time Series Database API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-writexl 

%description
An R API providing easy access to a relational database with
macroeconomic, financial and development related time series data for
Uganda. Overall more than 5000 series at varying frequency (daily,
monthly, quarterly, annual in fiscal or calendar years) can be accessed
through the API. The data is provided by the Bank of Uganda, the Ugandan
Ministry of Finance, Planning and Economic Development, the IMF and the
World Bank. The database is being updated once a month.

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
