%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SynthesizerPlus
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Synthetic Data Generation with Copulas, Evaluation and Multi-Format I/O

License:          EUPL (>= 1.2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Generates synthetic versions of numeric, categorical, mixed-type and
time-series data. Marginal distributions are modelled with interpolated
empirical quantile functions and dependence with Gaussian or Student-t
copulas (Sklar, 1959). Discrete and categorical variables enter the copula
through the distributional transform (Ruschendorf, 2009,
<doi:10.1016/j.jspi.2009.05.030>), and their latent correlations are
estimated by maximum likelihood as polychoric (Olsson, 1979,
<doi:10.1007/BF02296207>) and polyserial (Olsson, Drasgow and Dorans,
1982, <doi:10.1007/BF02294164>) correlations. Missing values are modelled
by missingness indicators inside the copula, so that missingness may
depend on other variables. Supports stratified models, a closeness
parameter with calibration to a target distance or disclosure-risk level,
chunked generation of very large data sets, copula vector-autoregressive
and bootstrap time-series synthesis, augmentation of small training sets
for machine learning, and random generation from multivariate
distributions and elliptical and Archimedean copulas. Fidelity, utility
and disclosure risk are assessed with marginal distances, association
matrices, propensity score mean-squared error (Snoke et al., 2018,
<doi:10.1111/rssa.12358>), confidence-interval overlap, correct
attribution probability and distance to closest record, with 'ggplot2'
visualisations. Data can be read from and written to CSV, TSV, RDS, RData,
Parquet, Feather, HDF5, JSON, NDJSON, Excel, SPSS, Stata, SAS and fst
files. The empirical-quantile and copula approach builds on ideas of the
'synthesizer' package by Mark van der Loo.

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
