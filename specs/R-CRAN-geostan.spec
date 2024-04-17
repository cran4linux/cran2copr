%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geostan
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Matrix >= 1.3
BuildRequires:    R-CRAN-sf >= 1.0.10
BuildRequires:    R-CRAN-spdep >= 1.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-signs 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-Matrix >= 1.3
Requires:         R-CRAN-sf >= 1.0.10
Requires:         R-CRAN-spdep >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-signs 
Requires:         R-CRAN-gridExtra 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
For Bayesian inference with spatial data, provides exploratory spatial
analysis tools, multiple spatial model specifications, spatial model
diagnostics, and special methods for inference with small area survey data
(e.g., the America Community Survey (ACS)) and censored population health
surveillance data. Models are pre-specified using the Stan programming
language, a platform for Bayesian inference using Markov chain Monte Carlo
(MCMC). References: Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>;
Donegan (2021) <doi:10.31219/osf.io/3ey65>; Donegan (2022)
<doi:10.21105/joss.04716>; Donegan, Chun and Hughes (2020)
<doi:10.1016/j.spasta.2020.100450>; Donegan, Chun and Griffith (2021)
<doi:10.3390/ijerph18136856>; Morris et al. (2019)
<doi:10.1016/j.sste.2019.100301>.

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
