%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contoso
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Dataset of the 'Contoso' Company

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-duckdb >= 1.4.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-duckdb >= 1.4.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-assertthat 

%description
A collection of synthetic datasets simulating sales transactions from a
fictional company. The dataset includes various related tables that
contain essential business and operational data, useful for analyzing
sales performance and other business insights. Key tables included in the
package are: - "sales": Contains data on individual sales transactions,
including order details, pricing, quantities, and customer information. -
"customer": Stores customer-specific details such as demographics,
geographic location, occupation, and birthday. - "store": Provides
information about stores, including location, size, status, and
operational dates. - "orders": Contains details about customer orders,
including order and delivery dates, store, and customer data. - "product":
Contains data on products, including attributes such as product name,
category, price, cost, and weight. - "date": A time-based table that
includes date-related attributes like year, month, quarter, day, and
working day indicators. This dataset is ideal for practicing data
analysis, performing time-series analysis, creating reports, or simulating
business intelligence scenarios.

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
