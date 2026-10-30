%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoecu
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maps of the Provinces, Cantons and Parishes of Ecuador (Mapas de Provincias, Cantones y Parroquias del Ecuador)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides the boundaries of the provinces, cantons and parishes of Ecuador
as 'sf' objects, identified by the codes of the national
political-administrative division (DPA, "División
Político-Administrativa"), ready to be mapped and joined with health,
epidemiological surveillance or other data. The three levels nest exactly
and are offered in two resolutions: a light one for maps and dashboards
and a detailed one for spatial analysis. The layers are derived from the
open data of the Territorial Organization of the State published by the
National Committee of Internal Boundaries (CONALI, Ministry of Government
of Ecuador) under a CC BY licence <https://www.datosabiertos.gob.ec/>, and
are downloaded on first use as 'GeoPackage' files, verified and cached
locally. Includes a catalogue of DPA codes, a table to update codes from
earlier versions, helpers to clean codes and place names, and tools to
relocate the Galapagos Islands in national maps. Documentation is in
Spanish.

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
