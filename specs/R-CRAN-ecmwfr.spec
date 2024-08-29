%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecmwfr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'ECMWF' and 'CDS' Data Web Services

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-keyring 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-keyring 

%description
Programmatic interface to the European Centre for Medium-Range Weather
Forecasts dataset web services (ECMWF; <https://www.ecmwf.int/>) and
Copernicus's Data Stores. Allows for easy downloads of weather forecasts
and climate reanalysis data in R. Data stores covered include the Climate
Data Store (CDS; <https://cds-beta.climate.copernicus.eu>), Atmosphere
Data Store (ADS; <https://ads-beta.atmosphere.copernicus.eu>) and Early
Warning Data Store (CEMS; <https://ewds-beta.climate.copernicus.eu>).

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
