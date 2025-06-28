%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataRetrieval
%global packver   2.7.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.19
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieval Functions for USGS and EPA Hydrology and Water Quality Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 6.0.0
BuildRequires:    R-CRAN-lubridate >= 1.5.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-curl >= 6.0.0
Requires:         R-CRAN-lubridate >= 1.5.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-sf 

%description
Collection of functions to help retrieve U.S. Geological Survey and U.S.
Environmental Protection Agency water quality and hydrology data from web
services.

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
