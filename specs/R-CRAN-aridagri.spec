%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aridagri
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Statistical Tools for Agricultural Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch

%description
A comprehensive suite of statistical and analytical tools for agricultural
research. Includes complete analysis of variance (ANOVA) functions for all
experimental designs: Completely Randomized Design (CRD), Randomized Block
Design (RBD), Pooled RBD, Split Plot with all variations, Split-Split
Plot, Strip Plot, Latin Square, Factorial, Augmented, and Alpha Lattice,
with proper error terms and comprehensive Standard Error (SE) and Critical
Difference (CD) calculations. Features multiple post-hoc tests: Least
Significant Difference (LSD), Duncan Multiple Range Test (DMRT), Tukey
Honestly Significant Difference (HSD), Student-Newman-Keuls (SNK),
Scheffe, Bonferroni, and Dunnett, along with assumption checking and
publication-ready output. Advanced methods include stability analysis
using Eberhart-Russell regression, Additive Main Effects and
Multiplicative Interaction (AMMI), Finlay-Wilkinson regression, Shukla
stability variance, Wricke ecovalence, Coefficient of Variation (CV), and
Cultivar Superiority Index as described in Eberhart and Russell (1966)
<doi:10.2135/cropsci1966.0011183X000600010011x>. Thermal indices include
Growing Degree Days (GDD), Heliothermal Units (HTU), Photothermal Units
(PTU), and Heat Use Efficiency (HUE). Crop growth analysis covers Crop
Growth Rate (CGR), Relative Growth Rate (RGR), Net Assimilation Rate
(NAR), and Leaf Area Index (LAI). Also provides harvest index, yield gap
analysis, economic efficiency indices (Benefit-Cost ratio), nutrient use
efficiency calculations, correlation matrix, Principal Component Analysis
(PCA), path analysis, and Structural Equation Modeling (SEM). Statistical
methods follow Gomez and Gomez (1984, ISBN:0471870927) and Panse and
Sukhatme (1985, ISBN:8170271169).

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
