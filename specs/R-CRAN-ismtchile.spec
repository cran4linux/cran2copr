%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ismtchile
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Socio Material Territorial Index

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 

%description
Paquete creado con el fin de facilitar el cálculo y distribución del
índice Socio Material Territorial (ISMT), elaborado por el Observatorio de
Ciudades UC. La metodología completa está disponible en "ISMT"
(<https://ideocuc-ocuc.hub.arcgis.com/datasets/6ed956450cfc4293b7d90df3ce3474e4/about>)
[Observatorio de Ciudades UC (2019)]. || Package created to facilitate the
calculation and distribution of the Socio-Material Territorial Index by
Observatorio de Ciudades UC. The full methodology is available at "ISMT"
(<https://ideocuc-ocuc.hub.arcgis.com/datasets/6ed956450cfc4293b7d90df3ce3474e4/about>)
[Observatorio de Ciudades UC (2019)].

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
