%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tesouror
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access Brazilian National Treasury Open Data APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-janitor >= 2.2.0
BuildRequires:    R-CRAN-stringi >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-janitor >= 2.2.0
Requires:         R-CRAN-stringi >= 1.7.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0

%description
Provides a unified interface to access open data from the Brazilian
National Treasury ('Tesouro Nacional') and related government APIs. Covers
six data sources: 'SICONFI'
<https://apidatalake.tesouro.gov.br/docs/siconfi/> for fiscal reports
('RREO', 'RGF', 'DCA', 'MSC') and entity information; 'CUSTOS'
<https://apidatalake.tesouro.gov.br/docs/custos/> for federal government
cost data; 'SADIPEM' <https://apidatalake.tesouro.gov.br/docs/sadipem/>
for public debt and credit operations; 'Transferencias Constitucionais'
<https://apiapex.tesouro.gov.br/aria/v1/transferencias_constitucionais/docs>
for constitutional transfers to states and municipalities; 'SIORG'
<https://estruturaorganizacional.dados.gov.br> for federal organizational
structure; and 'SIOPE' ('FNDE'/'MEC') for education spending data.
Features automatic pagination, in-memory caching, retry logic, and tidy
output.

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
