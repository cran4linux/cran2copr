%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aquats
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Ecological and Fisheries Data Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-vegan 

%description
A comprehensive statistical and visualization toolkit tailored for
observational data in fisheries science and aquatic ecology. Provides
streamlined workflows for univariate and factorial analysis of variance
(ANOVA), analysis of covariance (ANCOVA), multivariate analysis of
variance (MANOVA), permutational multivariate analysis of variance
(PERMANOVA), similarity percentages (SIMPER), generalized linear models,
non-linear morphometric regressions, two-group hypothesis testing, and
chi-square tests. Features multivariate ordination methods including
non-metric multidimensional scaling (NMDS), principal component analysis
(PCA), redundancy analysis (RDA), distance-based redundancy analysis
(db-RDA), and hierarchical cluster dendrograms. Computes alpha diversity
metrics, species accumulation curves, water quality index (WQI) values,
heavy metal ecotoxicological contamination indices, correlation heatmaps,
and Mantel test network linkages. Offers specialized environmental
visualizations including Sankey diagrams, Likert plots, circular bar
charts, and longitudinal time-series with uncertainty ribbons.
Methodological formulations for multivariate permutation tests follow
Anderson (2001) <doi:10.1111/j.1442-9993.2001.01070.pp.x>. Ecological
community dissimilarity transformations follow Legendre and Gallagher
(2001) <doi:10.1007/s004420100716>, and ecotoxicological contamination
index models follow Tomlinson et al. (1980) <doi:10.1007/BF02414780>.

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
