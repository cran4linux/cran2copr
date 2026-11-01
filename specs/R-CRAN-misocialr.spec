%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misocialr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access the Brazilian 'MDS' Social Information Matrix ('MI Social') API from 'R'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-httr2 >= 1.0.4
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-httr2 >= 1.0.4
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
'Tidyverse'-friendly interface to the 'MI Social' API of the Brazilian
Ministry of Development and Social Assistance ('MDS', 'SAGI')
<https://aplicacoes.mds.gov.br/sagi/servicos/misocial>. Retrieves monthly
municipal series of the 'Cadastro Unico' (registered families and people
by income bracket), the 'Bolsa Familia' programme (beneficiary families,
benefits and transfers), the 'BPC' benefit, the social assistance network
('CRAS', 'CREAS' and other units), 'SUAS' funding, 'Bolsa Familia'
conditionality monitoring and food security programmes as tidy long-format
'tibbles'.

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
