%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blavaan
%global packver   0.5-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.10
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Latent Variable Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-loo >= 2.0
BuildRequires:    R-CRAN-BH >= 1.69.0
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-lavaan >= 0.6.18
BuildRequires:    R-CRAN-nonnest2 >= 0.5.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-tmvnsim 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-loo >= 2.0
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-lavaan >= 0.6.18
Requires:         R-CRAN-nonnest2 >= 0.5.7
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-tmvnsim 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rstantools

%description
Fit a variety of Bayesian latent variable models, including confirmatory
factor analysis, structural equation models, and latent growth curve
models. References: Merkle & Rosseel (2018) <doi:10.18637/jss.v085.i04>;
Merkle et al. (2021) <doi:10.18637/jss.v100.i06>.

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
