%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yfscreen
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Yahoo Finance 'screener' API

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 

%description
Simple and efficient access to Yahoo Finance's 'screener' API
<https://finance.yahoo.com/research-hub/screener/> for querying and
retrieval of financial data. The core functionality abstracts the
complexities of interacting with Yahoo Finance APIs, such as session
management, crumb and cookie handling, query construction, pagination, and
JSON payload generation. This abstraction allows users to focus on
filtering and retrieving data rather than managing API details. Use cases
include screening across a range of security types including equities,
mutual funds, ETFs, indices, and futures. The package supports advanced
query capabilities, including logical operators, nested filters, and
customizable payloads. It automatically handles pagination to ensure
efficient retrieval of large datasets by fetching results in batches of up
to 250 entries per request. Filters can be dynamically defined to
accommodate a wide range of screening needs. The implementation leverages
standard HTTP libraries to handle API interactions efficiently and
provides support for both R and Python to ensure accessibility for a broad
audience.

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
