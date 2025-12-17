%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dawaR
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          An API Wrapper for 'DAWA' - 'The Danish Address Web API'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyRSS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-utils 
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyRSS 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-curl 
Requires:         R-utils 

%description
Functions for interacting with all sections of the official 'Danish
Address Web API' (also known as 'DAWA') <https://api.dataforsyningen.dk>.
The development of this package is completely independent from the
government agency, Klimadatastyrelsen, who maintains the API.

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
