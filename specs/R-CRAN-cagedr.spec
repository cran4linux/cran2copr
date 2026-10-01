%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cagedr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Novo CAGED Microdata from the Brazilian Ministry of Labour

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.7.0
BuildRequires:    R-CRAN-archive >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-stringi >= 1.7.0
Requires:         R-CRAN-archive >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0

%description
Download and read the public, non-identified microdata of the Novo CAGED
(Cadastro Geral de Empregados e Desempregados), the monthly registry of
formal employment movements published by the Brazilian Ministry of Labour
and Employment through the PDET FTP server
<ftp://ftp.mtps.gov.br/pdet/microdados/>. Lists the reference months
available on the server, downloads the three monthly files (movements
declared on time, declared late, and exclusions) with an idempotent local
cache, and reads the national 7z archives as a stream, filtering by state
and selecting columns before anything is kept in memory, so that a single
state can be extracted without loading the full national file. Also
provides the official record layout and a helper to consolidate
admissions, separations and net balance by reference month.

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
