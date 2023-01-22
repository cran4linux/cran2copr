%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  restatapi
%global packver   0.14.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.1
Release:          1%{?dist}%{?buildtag}
Summary:          Search and Retrieve Data from Eurostat Database

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-xml2 

%description
Eurostat is the statistical office of the European Union and provides high
quality statistics for Europe. Large set of the data is disseminated
through the Eurostat database
(<https://ec.europa.eu/eurostat/web/main/data/database>). The tools are
using the REST API with the Statistical Data and Metadata eXchange (SDMX)
Web Services
(<https://wikis.ec.europa.eu/pages/viewpage.action?pageId=44165555>) to
search and download data from the Eurostat database using the SDMX
standard.

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
