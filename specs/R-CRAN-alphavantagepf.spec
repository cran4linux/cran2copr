%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alphavantagepf
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive R Wrapper for 'Alphavantage Financial Data' API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate >= 4000
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-glue >= 1.1.1
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-lubridate >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-timeDate >= 4000
Requires:         R-utils >= 4.0.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-glue >= 1.1.1
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-lubridate >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-data.table 

%description
Download 'Alphavantage financial data'
<https://www.alphavantage.co/documentation/> to reduced 'data.table'
objects. Includes support functions to extract and simplify complex data
returned from API calls.

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
