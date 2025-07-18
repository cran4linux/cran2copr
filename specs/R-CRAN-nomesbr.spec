%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nomesbr
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Limpa e Simplifica Nomes de Pessoas (Name Cleaner and Simplifier)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tictoc 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tictoc 

%description
Limpa e simplifica nomes de pessoas para auxiliar no pareamento de banco
de dados na ausência de chaves únicas não ambíguas. Detecta e corrige
erros tipográficos mais comuns, simplifica opcionalmente termos sujeitos
eventualmente a omissão em cadastros, e simplifica foneticamente suas
palavras, aplicando variação própria do algoritmo metaphoneBR. (Cleans and
simplifies person names to assist in database matching when unambiguous
unique keys are unavailable. Detects and corrects common typos, optionally
simplifies terms prone to omission in records, and applies phonetic
simplification using a custom variation of the metaphoneBR algorithm.)
Mation (2025) <doi:10.6082/uchicago.15104>.

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
