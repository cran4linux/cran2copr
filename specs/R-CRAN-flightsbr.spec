%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flightsbr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Flight and Airport Data from Brazil

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-archive 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-parzer 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-archive 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-parzer 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-rvest 

%description
Download flight and airport data from Brazil’s Civil Aviation Agency
(ANAC) <https://www.gov.br/anac/pt-br>. The data covers detailed
information on aircraft, airports, and airport operations registered with
ANAC. It also includes data on airfares, all international flights to and
from Brazil, and domestic flights within the country.

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
