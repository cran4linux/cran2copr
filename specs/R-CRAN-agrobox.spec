%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agrobox
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
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
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-multcompView 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-agricolae 
Requires:         R-stats 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-multcompView 

%description
Set of tools for statistical analysis, visualization, and reporting of
agroindustrial and agricultural experiments. The package provides
functions to perform one-way and two-way ANOVA with post-hoc tests (Tukey
HSD and Duncan MRT), Welch ANOVA for heteroscedastic data, and the
Games-Howell post-hoc test as a robust alternative when variance
homogeneity fails. Normality of residuals is assessed with the
Shapiro-Wilk test and homoscedasticity with the Fligner-Killeen test; the
appropriate statistical path is selected automatically based on these
diagnostics. Coefficients of variation and statistical power (via one-way
ANOVA power analysis) are reported alongside the post-hoc letter display.
High-level wrappers allow automated multi-variable analysis with optional
clustering by one or two experimental factors, with support for custom
level ordering and relabeling. Results are returned as 'ggplot2' boxplots
with mean and letter annotations, wide-format summary tables ready for
publication or LaTeX rendering, and structured decision summaries for
rapid agronomic interpretation. Direct export to Excel spreadsheets and
high-resolution image tables is also supported. Functions follow methods
widely used in agronomy, field trials, and plant breeding. Key references:
Tukey (1949) <doi:10.2307/3001913>; Duncan (1955) <doi:10.2307/3001478>;
Welch (1951) <doi:10.2307/2332579>; Games and Howell (1976)
<doi:10.2307/2529858>; Shapiro and Wilk (1965) <doi:10.2307/2333709>;
Fligner and Killeen (1976) <doi:10.2307/2529096>; Cohen (1988,
ISBN:9781138892899); Wickham (2016, ISBN:9783319242750) for 'ggplot2'; see
also 'agricolae' <https://CRAN.R-project.org/package=agricolae> and
'rstatix' <https://CRAN.R-project.org/package=rstatix>. Version en
espanol: Conjunto de herramientas para el analisis estadistico,
visualizacion y generacion de reportes en ensayos agroindustriales y
agricolas. Incluye ANOVA univariado y bifactorial con pruebas post-hoc
(Tukey HSD y Duncan MRT), ANOVA de Welch para datos heterocedasticos y la
prueba post-hoc de Games-Howell como alternativa robusta cuando falla la
homogeneidad de varianzas. La normalidad de residuos se evalua con la
prueba de Shapiro-Wilk y la homogeneidad de varianzas con la prueba de
Fligner-Killeen; la ruta estadistica apropiada se selecciona
automaticamente segun estos diagnosticos. Se reportan coeficientes de
variacion y potencia estadistica junto con las letras de separacion de
medias. Los envoltorios de alto nivel permiten analisis multivariable
automatizado con agrupamiento opcional por uno o dos factores
experimentales, con soporte para orden y etiquetado personalizado de
niveles. Los resultados se devuelven como boxplots con anotaciones de
medias y letras, tablas resumen en formato ancho listas para publicacion o
renderizado en LaTeX, y resumenes de decision para interpretacion
agronomica rapida. Tambien se soporta exportacion directa a Excel e
imagenes de alta resolucion para informes tecnicos.

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
