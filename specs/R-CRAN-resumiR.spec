%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  resumiR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Medidas Resumen y Tablas de Frecuencia para Datos Numéricos / Summary Measures and Frequency Tables for Numerical Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 

%description
Permite obtener rápidamente una serie de medidas de resumen y gráficos
para datos numéricos discretos o continuos en series simples. También
permite obtener tablas de frecuencia clásicas y gráficos cuando se desea
realizar un análisis de series agrupadas. Su objetivo es de aplicación
didáctica para un curso introductorio de Bioestadística utilizando el
software R, para las carreras de grado las carreras de grado y otras
ofertas educativas de la Facultad de Ciencias Agrarias de la UNJu / It
generates summary measures and graphs for discrete or continuous numerical
data in simple series. It also enables the creation of classic frequency
tables and graphs when analyzing grouped series. Its purpose is for
educational application in an introductory Biostatistics course using the
R software, aimed at undergraduate programs and other educational
offerings of the Faculty of Agricultural Sciences at the National
University of Jujuy (UNJu).

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
