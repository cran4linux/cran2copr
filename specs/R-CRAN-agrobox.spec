%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agrobox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Visualization and Statistical Tools for Agroindustrial Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-agricolae 
Requires:         R-stats 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-rlang 

%description
Set of functions to create clear graphics and run common statistical
analyses for agricultural experiments (ANOVA with post-hoc tests such as
Tukey HSD and Duncan MRR, coefficient of variation, and simple power
calculations), streamlining exploratory analysis and reporting. Functions
build on 'ggplot2' and base 'stats' and follow methods widely used in
agronomy (field trials, plant breeding). Key references include Tukey
(1949) <doi:10.2307/3001913>, Duncan (1955) <doi:10.2307/3001478>, Cohen
(1988, ISBN:9781138892899); see also 'agricolae'
<https://CRAN.R-project.org/package=agricolae> and Wickham (2016,
ISBN:9783319242750) for 'ggplot2'. Versión en español: Conjunto de
funciones para generar gráficos claros y ejecutar análisis habituales en
ensayos agrícolas (ANOVA con pruebas post-hoc como Tukey HSD y Duncan MRR,
coeficiente de variación y cálculos simples de potencia), facilitando el
análisis exploratorio y la elaboración de reportes. Los métodos
implementados se basan en Tukey (1949) <doi:10.2307/3001913>, Duncan
(1955) <doi:10.2307/3001478> y Cohen (1988, ISBN:9781138892899); ver
también 'agricolae' <https://CRAN.R-project.org/package=agricolae> y
Wickham (2016, ISBN:9783319242750) para 'ggplot2'.

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
