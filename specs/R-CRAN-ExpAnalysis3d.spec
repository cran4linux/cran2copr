%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExpAnalysis3d
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Pacote Para Analise De Experimentos Com Graficos De Superficie Resposta

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 

%description
Pacote para a analise de experimentos havendo duas variaveis explicativas
quantitativas e uma variavel dependente quantitativa. Os experimentos
podem ser sem repeticoes ou com delineamento estatistico. Sao ajustados 12
modelos de regressao multipla e plotados graficos de superficie resposta
(Hair JF, 2016) <ISBN:13:978-0138132637>.(Package for the analysis of
experiments having two explanatory quantitative variables and one
quantitative dependent variable. The experiments can be without
repetitions or with a statistical design. Twelve multiple regression
models are fitted and response surface graphs are plotted (Hair JF, 2016)
<ISBN:13:978-0138132637>).

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
