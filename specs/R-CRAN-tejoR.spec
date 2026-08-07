%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tejoR
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Harmonization of Territorial Series Across Changing Geographies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-utils 

%description
Builds, validates, seals and applies weighting matrices ('crosswalks') to
carry statistical series across changing zoning systems, such as the
transition from the 112 Unidades de Planeamiento Zonal (UPZ) to the 33
Unidades de Planeamiento Local (UPL) in Bogota (Decree 555 of 2021).
Implements the 'tejo-crosswalk/0.2' specification shared with the 'Python'
package 'tejo': 'sha256'-sealed artifacts, non-negative weights that sum
to one for each source unit, dasymetric weighting with vector ancillary
data via 'sf', rates that are never interpolated directly, and missing
values that propagate instead of being silently imputed. Methods: Tobler
(1979) <doi:10.1080/01621459.1979.10481647>; Mennis (2003)
<doi:10.1111/0033-0124.10042>. Descripcion en espanol: construye, valida,
sella y aplica matrices de ponderadores ('crosswalks') para trasladar
series estadisticas entre mallas geograficas que cambian, como la
transicion de UPZ a UPL en Bogota (Decreto 555 de 2021): integridad por
'sha256', pesos no negativos que suman uno por unidad fuente, metodo
dasimetrico con ancilar vectorial via 'sf', tasas que nunca se interpolan
directamente y valores faltantes que se propagan en lugar de imputarse.

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
