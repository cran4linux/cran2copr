%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mefdind
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Imports Data from MoE Spain

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Imports indicator data provided by the Ministry of Education (MoE),Spain.
The data is stored at
<https://www.educacionyfp.gob.es/servicios-al-ciudadano/estadisticas/no-universitaria.html>
Includes functions for reading, downloading, and selecting data for main
series. This package is not sponsored or supported by the MoE Spain.
Importa datos con indicadores del Ministerio de Educación y Formación
Profesional (MEFD) de Españá. Los datos están en
<https://www.educacionyfp.gob.es/servicios-al-ciudadano/estadisticas/no-universitaria.html>
Contiene funciones para leer, descargar, y seleccionar bases de datos de
series principales. Este paquete no es patrocinado o respaldado por el
MEFD.

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
