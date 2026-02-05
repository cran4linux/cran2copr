%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lsirm12pl
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Space Item Response Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GPArotation 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 

%description
Analysis of dichotomous, ordinal, and continuous response data using
latent space item response models (LSIRMs). Provides 1PL and 2PL LSIRMs
for binary response data as described in Jeon et al. (2021)
<doi:10.1007/s11336-021-09762-5>, extensions for continuous response data,
and graded response models (GRM) for Likert-scale ordinal data as
described in De Carolis et al. (2025) <doi:10.1080/00273171.2025.2605678>.
Supports Bayesian model selection with spike-and-slab priors, adaptive
MCMC algorithms, and methods for handling missing data under missing at
random (MAR) and missing completely at random (MCAR) assumptions. Provides
various diagnostic plots to inspect the latent space and summaries of
estimated parameters.

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
