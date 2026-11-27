%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  condepe
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access the Open Data of the Pernambuco Observatory

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-nanoparquet >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-nanoparquet >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-tibble 
Requires:         R-tools 

%description
A tidy interface to the open data of the Observatory of Pernambuco, Brazil
(<https://cf.pe.gov.br/observatorio>): municipal series on population,
economy, public finance, labour, education, health, security, transport
and environment, collected from official public sources (such as the
Brazilian Institute of Geography and Statistics and the Ministry of
Health, identified in every row) and organised by 'Condepe/Fidem', the
State Agency for Planning and Research, every source in the same long
format, returned as tibbles. Also provides the municipal boundaries and
eleven official regional classifications of the municipalities, ready for
maps, and citations that credit the original source. Files are read from
the canonical endpoint with a 'Hugging Face' mirror as fallback, cached on
disk per catalogue version and checked against their published 'SHA-256'.
Network failures are handled gracefully.

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
