%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eia
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          API Wrapper for 'US Energy Information Administration' Open Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readxl 

%description
Provides API access to data from the 'US Energy Information
Administration' ('EIA') <https://www.eia.gov/>. Use of the API requires a
free API key obtainable at <https://www.eia.gov/opendata/register.php>.
The package includes functions for searching 'EIA' data categories and
importing time series and geoset time series datasets. Datasets returned
by these functions are provided in a tidy format or alternatively in more
raw form. It also offers helper functions for working with 'EIA' date
strings and time formats and for inspecting different summaries of series
metadata. The package also provides control over API key storage and
caching of API request results.

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
