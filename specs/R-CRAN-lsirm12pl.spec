%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lsirm12pl
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Space Item Response Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
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
Analysis of dichotomous and continuous response data using latent factor
by both 1PL LSIRM and 2PL LSIRM as described in Jeon et al. (2021)
<doi:10.1007/s11336-021-09762-5>. It includes original 1PL LSIRM and 2PL
LSIRM provided for binary response data and its extension for continuous
response data. Bayesian model selection with spike-and-slab prior and
method for dealing data with missing value under missing at random,
missing completely at random are also supported. Various diagnostic plots
are available to inspect the latent space and summary of estimated
parameters.

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
