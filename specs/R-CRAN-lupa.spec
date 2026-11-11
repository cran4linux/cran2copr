%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lupa
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Profiling and Quality Measurement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-data.table 

%description
Profiles tabular data and measures its quality. Discovers structural
patterns, implicit types, mixed date formats and reusable findings about
potential data issues; defines quality frameworks with user-declared
dimensions, reusable metrics with explicit granularity and typed
aggregation; keeps versioned histories and detects structural drift;
writes self-contained HyperText Markup Language reports; and produces
editable cleaning plans that apply only the actions the user selects, with
an audit log. The general model follows Batini and Scannapieco (2016)
<doi:10.1007/978-3-319-24106-7>. The package implements version 1.6 of the
data quality management framework for digital government of the Uruguayan
Agency for Electronic Government and Information and Knowledge Society,
AGESIC (2020)
<https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/comunicacion/publicaciones/marco-trabajo-para-gestion-calidad-datos>;
an optional taxonomy of the fifteen characteristics of the standard 25012
of the International Organization for Standardization and the
International Electrotechnical Commission, ISO/IEC (2008)
<https://www.iso.org/standard/35736.html>; and the four levels and
nineteen principles of the national quality assurance framework of the
United Nations (2019)
<https://unstats.un.org/unsd/methodology/dataquality/>, as adapted for
Latin America and the Caribbean by the Statistical Conference of the
Americas of the Economic Commission for Latin America and the Caribbean,
CEA-CEPAL (2022) <https://repositorio.cepal.org/handle/11362/47464>.
AGESIC, CEA and CEPAL are the Spanish acronyms of these institutions.

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
