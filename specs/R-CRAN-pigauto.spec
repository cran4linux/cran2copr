%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pigauto
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fill in Missing Species Traits Using a Phylogenetic Tree

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-withr 

%description
Imputes missing species trait data for comparative analyses by combining
three sources of information: phylogenetic similarity (closely related
species share similar traits), cross-trait correlations (observed traits
inform missing ones), and optional environmental covariates (climate,
habitat, geography). Handles continuous measurements, counts, binary
variables, ordered categories, unordered categories, bounded proportions,
zero-inflated counts, and compositional multi-proportion data in a single
call. The method blends a phylogenetic baseline with a graph neural
network correction; a per-trait gate calibrated on held-out data ensures
the network only contributes when it improves on the baseline. Provides
conformal prediction intervals for continuous, count, and ordinal traits
and an experimental analysis-aware multiple-imputation workflow for one
missing continuous covariate in Gaussian linear, binomial-logit, and
Gaussian random-intercept models, with Rubin pooling limited to fixed
effects. Stochastic graph-network and posterior-tree completions are
prediction diagnostics rather than validated inferential imputations.
Tested up to 10,000 species. Bundled datasets include 300-species and
9,993-species bird-trait subsets with matching example phylogenetic trees.
Rubin (1987, ISBN:978-0-471-08705-2); Vovk et al. (2005,
ISBN:978-0-387-25061-8); Nakagawa and de Villemereuil (2019)
<doi:10.1093/sysbio/syy089>.

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
