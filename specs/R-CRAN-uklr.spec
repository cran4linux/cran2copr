%global __brp_check_rpaths %{nil}
%global packname  uklr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Client to United Kingdom Land Registry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httr >= 1.4.1

%description
Access data from Land Registry Open Data
<http://landregistry.data.gov.uk/> through 'SPARQL' queries. 'uklr'
supports the house price index, transaction and price paid data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
