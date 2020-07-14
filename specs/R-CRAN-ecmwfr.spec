%global packname  ecmwfr
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Interface to 'ECMWF' and 'CDS' Data Web Services

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-curl 

%description
Programmatic interface to the European Centre for Medium-Range Weather
Forecasts dataset web services (ECMWF; <https://www.ecmwf.int/>) and
Copernicus's Climate Data Store (CDS;
<https://cds.climate.copernicus.eu>). Allows for easy downloads of weather
forecasts and climate reanalysis data in R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
