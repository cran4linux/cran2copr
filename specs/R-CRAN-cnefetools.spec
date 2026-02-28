%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cnefetools
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Analysis of Brazilian CNEFE Address Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-geobr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-h3jsr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-duckspatial 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-piggyback 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-geobr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-h3jsr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-duckspatial 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-piggyback 

%description
Download, cache and read municipality-level address data from the Cadastro
Nacional de Enderecos para Fins Estatisticos (CNEFE) of the 2022 Brazilian
Census, published by the Instituto Brasileiro de Geografia e Estatistica
(IBGE)
<https://ftp.ibge.gov.br/Cadastro_Nacional_de_Enderecos_para_Fins_Estatisticos/>.
Beyond data access, provides spatial aggregation of addresses, computation
of land-use mix indices, and dasymetric interpolation of census tract
variables using CNEFE dwelling points as ancillary data. Results can be
produced on 'H3' hexagonal grids or user-supplied polygons, and heavy
operations leverage a 'DuckDB' backend with extensions for fast,
in-process execution.

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
