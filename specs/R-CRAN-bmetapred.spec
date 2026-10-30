%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bmetapred
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Meta-Prediction in the Presence of Prediction Error

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-loo 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits pseudo-Bayesian Model Averaging (pBMA) and Bayesian Stacking
ensembles of linear meta-models while explicitly accounting for the
prediction errors of the individual models, building on the Bayesian
Stacking of predictive distributions framework of Yao et al. (2018)
<doi:10.1214/17-BA1091>. When native uncertainty estimates are
unavailable, it provides tools to estimate heteroscedastic errors via
Local Polynomial Regression (LOESS). The meta-model space is explored
using exhaustive search, a Markov Chain Monte Carlo Model Composition
(MC3) algorithm following Madigan and Raftery (1994)
<doi:10.1080/01621459.1994.10476894> when pBMA is selected, or a
tabu-guided heuristic search with parallel tempering when bayesian
stacking is selected, all powered by 'brms' (Bürkner, 2017
<doi:10.18637/jss.v080.i01>).

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
