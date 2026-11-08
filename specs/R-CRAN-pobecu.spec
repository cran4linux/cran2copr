%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pobecu
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population of Ecuador by Province, Canton and Parish (Población del Ecuador por Provincia, Cantón y Parroquia)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides the official population estimates and projections of Ecuador
published by the National Institute of Statistics and Censuses (INEC,
"Instituto Nacional de Estadística y Censos"), Revision 2024: national
(1950-2050), provincial (1990-2035) and cantonal (2010-2035) figures by
sex, age and urban/rural area, identified by the codes of the
political-administrative division (DPA, "División
Político-Administrativa")
<https://www.ecuadorencifras.gob.ec/proyecciones-poblacionales/>. Because
INEC does not publish projections for parishes, the package also offers a
parish-level estimate for 2010-2035 that distributes the official cantonal
projection among parishes using their shares in the 2010 and 2022 censuses
(logistic extrapolation) and their age and sex structure in the 2022
census (iterative proportional fitting); parish figures always add up to
the official cantonal ones. Includes helpers to aggregate ages, join
population denominators to case tables and compute rates, convert codes of
urban parishes and of the 2026 political-administrative division (CONALI,
"Comité Nacional de Límites Internos") to census units, and native
integration with the 'geoecu' package to map population on the boundaries
of provinces, cantons and parishes. Documentation is in Spanish. Includes
conditional territorial population scenarios for 1900-2100 using
structural time series, damped extrapolation and hierarchical
compositional allocation with Monte Carlo bands.

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
