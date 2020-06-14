%global packname  MVar.pt
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          2%{?dist}
Summary:          Analise multivariada (brazilian portuguese)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-stats 

%description
Pacote para analise multivariada, tendo funcoes que executam analise de
correspondencia simples (CA) e multipla (MCA), analise de componentes
principais (PCA), analise de correlacao canonica (CCA), analise fatorial
(FA), escalonamento multidimensional (MDS), analise discriminante linear
(LDA) e quadratica (QDA), analise de cluster hierarquico e nao
hierarquico, regressao linear simples e multipla, analise de multiplos
fatores (MFA) para dados quantitativos, qualitativos, de frequencia
(MFACT) e dados mistos, projection pursuit (PP), grant tour e outras
funcoes uteis para a analise multivariada.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
