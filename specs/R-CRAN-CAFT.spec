%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CAFT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rank-Based Compositional Analysis using Log-Linear Models for Microbiome Data with Zero Cells

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Provides rank-based compositional differential abundance analysis for
microbiome count data with zero cells using the compositional accelerated
failure time model of Satten, Li and Zhao (2025) "CAFT: A Compositional
Log-Linear Model for Microbiome Data with Zero Cells"
<doi:10.1101/2025.11.26.690468>. Zero counts are treated as censored
observations below sample-specific detection limits, avoiding the use of
pseudocounts. The package implements estimation and hypothesis testing
procedures for assessing associations between microbial taxa and
covariates while accounting for the compositional structure of sequencing
count data. It supports taxon-level differential abundance analysis,
estimation of regression effects under censoring induced by detection
limits, and inference based on rank-based methods that remain applicable
in the presence of excess zeros. Functions are provided for model fitting,
significance testing, extraction of effect estimates, and summarization of
results across taxa. The package also provides optional bootstrap
calibration of taxon-level p-values for sensitivity analysis in
small-taxon settings.

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
