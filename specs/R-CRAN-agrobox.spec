%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agrobox
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
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
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-agricolae 
Requires:         R-stats 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-openxlsx 

%description
Set of tools for statistical analysis, visualization, and reporting of
agroindustrial and agricultural experiments. The package provides
functions to perform ANOVA with post-hoc tests (e.g. Tukey HSD and Duncan
MRR), compute coefficients of variation, and generate publication-ready
summaries. High-level wrappers allow automated multi-variable analysis
with optional clustering by experimental factors, as well as direct export
of results to Excel spreadsheets and high-resolution image tables for
reporting. Functions build on 'ggplot2', 'stats', and related packages and
follow methods widely used in agronomy (field trials and plant breeding).
Key references include Tukey (1949) <doi:10.2307/3001913>, Duncan (1955)
<doi:10.2307/3001478>, and Cohen (1988, ISBN:9781138892899); see also
'agricolae' <https://CRAN.R-project.org/package=agricolae> and Wickham
(2016, ISBN:9783319242750> for 'ggplot2'. Versión en español: Conjunto de
herramientas para el análisis estadístico, visualización y generación de
reportes en ensayos agroindustriales y agrícolas. Incluye funciones para
ANOVA con pruebas post-hoc, resúmenes automáticos multivariables con o sin
agrupamiento por factores, y exportación directa de resultados a Excel e
imágenes de alta resolución para informes técnicos.

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
