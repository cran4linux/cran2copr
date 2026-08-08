%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  censosbo
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Analysis of Bolivian Census Microdata

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow >= 14.0.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-arrow >= 14.0.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 

%description
Programmatic access to the microdata of the Bolivian population and
housing censuses of 1976, 1992, 2001, 2012 and 2024, published by the
National Statistics Institute of Bolivia (INE, <https://www.ine.gob.bo/>).
Data files in Apache Parquet format are downloaded on demand from a
companion data repository, cached locally, and can be filtered by
department, province or municipality. Supports 'dplyr' workflows through
Apache Arrow and SQL queries through 'DuckDB'. Includes variable
dictionaries for every census year with a thematic taxonomy and contextual
metadata (reference population, questionnaire item number and provenance
of each variable), derived from the census questionnaires and from the
Data Documentation Initiative (DDI) files of the INE ANDA catalogue;
functions to harmonise variables across censuses for temporal comparison;
and choropleth maps at the department and municipality level. Also
includes the 2024 census aggregates for urban blocks and rural
communities, with their geometries. Documentation and messages are in
Spanish, the language of the source data.

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
