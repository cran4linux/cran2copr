%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  electedBR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Brazilian Election Winners and Sitting Members of Congress

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-nanoparquet 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-nanoparquet 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Retrieves the candidates elected in Brazilian municipal and general
elections since 2018, consolidated from the open data of the Superior
Electoral Court (TSE, <https://dadosabertos.tse.jus.br/>) and distributed
as yearly Parquet files, together with the federal deputies and senators
currently serving according to the open data APIs of the Chamber of
Deputies (<https://dadosabertos.camara.leg.br/>) and the Federal Senate
(<https://www12.senado.leg.br/dados-abertos>). Election results and
current office holding are kept as distinct queries; electoral roles,
service history and provenance are preserved. Every function returns a
tibble with English column names and has a Portuguese alias.

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
