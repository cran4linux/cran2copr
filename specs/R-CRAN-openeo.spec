%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  openeo
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Client Interface for 'openEO' Servers

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 0.2.2
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-IRdisplay 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-httr2 >= 0.2.2
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-IRdisplay 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 

%description
Access data and processing functionalities of 'openEO' compliant back-ends
in R.

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
