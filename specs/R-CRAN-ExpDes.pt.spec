%global packname  ExpDes.pt
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Pacote Experimental Designs (Portuguese)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stargazer 
Requires:         R-CRAN-stargazer 

%description
Pacote destinado a analise de delineamentos experimentais simples (DIC,
DBC e DQL), experimentos em esquema de fatorial duplo (em DIC e DBC),
experimentos em esquema de parcelas subdivididas no tempo (em DIC e DBC),
experimentos em esquema de fatorial duplo com um tratamento adicional (em
DIC e DBC), experimentos em esquema de fatorial triplo (em DIC e DBC) e
experimentos em esquema de fatorial triplo com um tratamento adicional (em
DIC e DBC); realizando a analise de variancia e comparacao de medias pelo
ajuste de modelos de regressao ate o terceiro grau (tratamentos
quantitativos) ou por testes de comparacao multipla: teste de Tukey, teste
de Student-Newman-Keuls (SNK), teste de Scott-Knott, teste de Duncan,
teste t (LSD), teste t de Bonferroni (LSD protegido) e teste Bootstrap
(tratamentos qualitativos); analise de residuos (Ferreira, Cavalcanti e
Nogueira (2014) <doi:10.4236/am.2014.519280>).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
