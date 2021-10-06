%global __brp_check_rpaths %{nil}
%global packname  ExpDes.pt
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Pacote Experimental Designs (Portugues)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stargazer 
Requires:         R-CRAN-stargazer 

%description
Pacote para análise de delineamentos experimentais (DIC, DBC e DQL),
experimentos em esquema fatorial duplo (em DIC e DBC), experimentos em
parcelas subdivididas (em DIC e DBC), experimentos em esquema fatorial
duplo com um tratamento adicional (em DIC e DBC), experimentos em fatorial
triplo (em DIC e DBC) e experimentos em esquema fatorial triplo com um
tratamento adicional (em DIC e DBC), fazendo analise de variancia e
comparacao de multiplas medias (para tratamentos qualitativos), ou
ajustando modelos de regressao ate a terceira potencia (para tratamentos
quantitativos); analise de residuos (Ferreira, Cavalcanti and Nogueira,
2014) <doi:10.4236/am.2014.519280>.

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
