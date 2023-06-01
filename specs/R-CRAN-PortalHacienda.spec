%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PortalHacienda
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Acceder Con R a Los Datos Del Portal De Hacienda

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.12
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-timetk >= 2.0
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-xts >= 0.12.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-forecast >= 8.12
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-timetk >= 2.0
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-purrr 

%description
Obtener listado de datos, acceder y extender series del Portal de Datos de
Hacienda.Las proyecciones se realizan con 'forecast', Hyndman RJ,
Khandakar Y (2008) <doi:10.18637/jss.v027.i03>. Search, download and
forecast time-series from the Ministry of Economy of Argentina. Forecasts
are built with the 'forecast' package, Hyndman RJ, Khandakar Y (2008)
<doi:10.18637/jss.v027.i03>.

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
