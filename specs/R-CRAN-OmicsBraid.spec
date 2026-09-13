%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OmicsBraid
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Covariance-Aware Inference of Cross-Omic Effect Trajectories

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
A research-oriented statistical framework for comparing standardized
biological effects across matched omics layers. It estimates
layer-specific standardized effects, accounts for cross-omic dependence
using matched-subject bootstrap correlations, tests multivariate omnibus
evidence, synthesizes consensus effects with generalized least squares,
quantifies cross-omic heterogeneity, performs practical-equivalence
testing, fits covariance-aware ordered GLS effect trajectories, classifies
hierarchical cross-layer effect patterns with separate confirmatory and
suggestive states, supports analytic and subject-bootstrap confidence
intervals for layer and consensus effects, supports empirical
matched-subject permutation and centered-bootstrap calibration of omnibus
and heterogeneity tests for non-Gaussian settings, and creates
evidence-forest and effect-braid visualizations. The package is designed
for analysis-ready bulk multi-omics data or externally estimated summary
statistics. It does not perform raw sequencing or mass-spectrometry
preprocessing. Methodological components draw on standardized
mean-difference estimation described by Hedges (1981)
<doi:10.3102/10769986006002107>, bootstrap resampling described by Efron
(1979) <doi:10.1214/aos/1176344552>, and two one-sided equivalence testing
described by Schuirmann (1987) <doi:10.1007/BF01068419>.

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
