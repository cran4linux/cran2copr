%global __brp_check_rpaths %{nil}
%global packname  rnmamod
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Network Meta-Analysis with Missing Participants

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-gemtc 
BuildRequires:    R-CRAN-ggfittext 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mcmcplots 
BuildRequires:    R-CRAN-netmeta 
BuildRequires:    R-CRAN-pcnetmeta 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-gemtc 
Requires:         R-CRAN-ggfittext 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mcmcplots 
Requires:         R-CRAN-netmeta 
Requires:         R-CRAN-pcnetmeta 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-writexl 

%description
A comprehensive suite of functions to perform and visualise pairwise and
network meta-analysis with aggregate binary or continuous missing
participant outcome data. The package covers core Bayesian one-stage
models implemented in a systematic review with multiple interventions,
including fixed-effect and random-effects network meta-analysis,
meta-regression, evaluation of the consistency assumption via the
node-splitting approach and the unrelated mean effects model, and
sensitivity analysis. Missing participant outcome data are addressed in
all models of the package. The package also offers a rich, user-friendly
visualisation toolkit that aids in appraising and interpreting the results
thoroughly and preparing the manuscript for journal submission. The
visualisation tools comprise the network plot, forest plots, panel of
diagnostic plots, heatmaps on the extent of missing participant outcome
data in the network, league heatmaps on estimation and prediction,
rankograms, Bland-Altman plot, leverage plot, deviance scatterplot,
heatmap of robustness, and barplot of Kullback-Leibler divergence. The
package also allows the user to export the results to an Excel file at the
working directory.

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
