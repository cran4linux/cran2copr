%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  precviasBR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Data of Road Precariousness in Brazil

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
Fornece acesso eficiente à malha espacial de precariedade viária
brasileira. O pacote realiza o download em cache e a leitura otimizada
(via Apache Arrow) de arquivos Parquet particionados, contendo o
cruzamento de variáveis de infraestrutura do Entorno do Censo Demográfico
2022 (IBGE) com a malha viária aberta do Overture Maps. [English] Provides
efficient access to the spatial network of road precariousness in Brazil.
The package performs cached downloads and optimized reading (via Apache
Arrow) of partitioned Parquet files. These files contain the intersection
of infrastructure variables from the 2022 Demographic Census (IBGE) with
the open street network from Overture Maps. Methodology and datasets are
detailed in Passos (2026) <doi:10.5281/zenodo.19711448>.

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
