%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARDECO
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Annual Regional Database of the European Commission (ARDECO)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ghql 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ghql 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-tidyr 

%description
A set of functions to access the 'ARDECO' (Annual Regional Database of the
European Commission) data directly from the official ARDECO public
repository through the exploitation of the 'ARDECO' APIs. The APIs are
completely transparent to the user and the provided functions provide a
direct access to the 'ARDECO' data. The 'ARDECO' database is a collection
of variables related to demography, employment, labour market, domestic
product, capital formation. Each variable can be exposed in one or more
units of measure as well as refers to total values plus additional
dimensions like economic sectors, gender, age classes. Data can be also
aggregated at country level according to the tercet classes as defined by
EUROSTAT. The description of the 'ARDECO' database can be found at the
following URL <https://urban.jrc.ec.europa.eu/ardeco>.

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
