%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  estbanr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Brazilian Monthly Banking Statistics by Municipality (ESTBAN)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.7.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-stringi >= 1.7.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 

%description
Download, read and tidy the ESTBAN (Estatistica Bancaria Mensal por
Municipio, Monthly Banking Statistics by Municipality) files published by
the Brazilian Central Bank (Banco Central do Brasil) for every bank branch
and municipality in Brazil. Each file reports balance-sheet accounts of
the COSIF (Plano Contabil das Instituicoes do Sistema Financeiro Nacional,
the chart of accounts of the Brazilian financial system) such as credit
operations, deposits and savings. Files are fetched from the official site
<https://www.bcb.gov.br/estatisticas/estatisticabancariamunicipios> with
an idempotent local cache, read from their Latin-1 encoded CSV
(comma-separated values) layout into tibbles, optionally filtered by
state, and aggregated by municipality. Includes tools to detect and impute
institution-month non-reports (an institution present in the file with
every account equal to zero), which would otherwise be mistaken for zero
balances.

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
