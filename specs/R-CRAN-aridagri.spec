%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aridagri
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Statistical Tools for Agricultural Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-utils 

%description
Analysis of variance for the experimental designs used in agricultural
research, with the correct error term for every stratum, standard error of
mean (SEm), standard error of difference (SEd), critical difference (CD),
coefficient of variation (CV) and letter groupings: completely randomized
design (CRD), randomized complete block design (RCBD) with missing plots,
Latin square, two- and three-factor factorials, split-plot designs
(including factorial main or sub-plots), split-split-plot and strip-plot
designs, and combined analysis over environments. Also covers the
augmented randomized complete block design with adjusted means and genetic
parameters (Federer, 1961 <doi:10.2307/2527837>), alpha lattice designs
with intra-block or residual maximum likelihood (REML) analysis (Patterson
and Williams, 1976 <doi:10.1093/biomet/63.1.83>) and repeated measures
with Greenhouse-Geisser and Huynh-Feldt corrections and covariance
structure models. Mean comparisons (least significant difference, Duncan,
Tukey, Student-Newman-Keuls, Scheffe, Bonferroni and Dunnett) follow Gomez
and Gomez (1984, ISBN:0471870927), with letters assigned by the algorithm
of Piepho (2004) <doi:10.1198/1061860043515>. Stability analysis includes
Eberhart and Russell (1966)
<doi:10.2135/cropsci1966.0011183X000600010011x> regression, additive main
effects and multiplicative interaction (AMMI), Finlay-Wilkinson, Shukla,
Wricke, coefficient of variation and Lin-Binns methods, and genotype plus
genotype-by-environment (GGE) biplots (Yan et al., 2000
<doi:10.2135/cropsci2000.403597x>). Further tools compute growing degree
days, helio-thermal and photo-thermal units, crop growth rate, relative
growth rate, net assimilation rate, leaf area index and leaf area
duration, harvest index, yield gaps with the technology index, nutrient
use efficiency, quadratic, plateau and Mitscherlich response curves with
the economic optimum dose, benefit-cost ratio, correlation, principal
component, path and structural equation analysis, publication tables for
many traits and figures.

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
