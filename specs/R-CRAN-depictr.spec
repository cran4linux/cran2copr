%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depictr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Unified Toolkit for Visualising Statistical Models and Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-patchwork >= 1.3.0
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-patchwork >= 1.3.0
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 

%description
A cohesive, publication-ready toolkit of plots that span the whole
analysis workflow with one consistent look. It covers exploratory data
analysis (distributions, categorical summaries, bivariate plots,
scatter-plot matrices, correlation heatmaps, missing-data maps, outliers,
estimation statistics and descriptive tables); multivariate analysis,
clustering with diagnostics and Kaplan-Meier survival curves; time series
(trends, autocorrelation, decomposition, seasonality and forecasting);
model estimates and inference (forest plots, model comparison, frequentist
and Bayesian estimates, predicted values, interactions, random effects and
optimiser checks); diagnostics and classification (residual panels, binned
residuals, influence, quantile-quantile, receiver operating characteristic
(ROC) curves, calibration, threshold tuning and confusion matrices);
uncertainty and power; and reporting helpers (a shared theme,
colourblind-aware palettes, plot composition and saving). Every plotting
function returns a 'ggplot2' object (or a 'patchwork' object for composite
panels), heavier modelling back-ends are optional, and the package ships
with reproducibly simulated datasets so that every example and vignette
runs without further setup.

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
