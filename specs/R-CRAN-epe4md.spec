%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epe4md
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          EPE's 4MD Model to Forecast the Adoption of Distributed Generation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jrvFinance 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fabletools 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-scales 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jrvFinance 
Requires:         R-CRAN-janitor 
Requires:         R-stats 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fabletools 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-future 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
EPE's (Empresa de Pesquisa Energética) 4MD (Modelo de Mercado da Micro e
Minigeração Distribuída - Micro and Mini Distributed Generation Market
Model) model to forecast the adoption of Distributed Generation. Given the
user's assumptions, it is possible to estimate how many consumer units
will have distributed generation in Brazil over the next 10 years, for
example. In addition, it is possible to estimate the installed capacity,
the amount of investments that will be made in the country and the monthly
energy contribution of this type of generation.
<https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-689/topico-639/NT_Metodologia_4MD_PDE_2032_VF.pdf>.

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
