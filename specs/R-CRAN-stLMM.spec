%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stLMM
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial and Space-Time Linear Mixed Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-BayesLogit >= 2.4
BuildRequires:    R-CRAN-Matrix >= 1.7.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
Requires:         R-CRAN-BayesLogit >= 2.4
Requires:         R-CRAN-Matrix >= 1.7.0
Requires:         R-CRAN-coda 
Requires:         R-stats 

%description
Fits Bayesian linear mixed models for spatial and space-time data with
fixed effects, independent and identically distributed (iid) grouped
random effects, and structured latent processes. The formula interface
supports first-order autoregressive (AR(1)) effects, dense Gaussian
processes, nearest-neighbor Gaussian processes, proper and Leroux
conditional autoregressive (CAR) effects, ordered directed acyclic graph
autoregressive (DAGAR) effects, separable CAR-time and DAGAR-time effects,
and spatially varying coefficients. The sampler uses sparse precision
matrix calculations when available and includes post-fitting tools for
latent process recovery, fitted values, prediction, pointwise log
likelihoods, and posterior sample extraction. Method details include Datta
et al. (2016) <doi:10.1080/01621459.2015.1044091>, Finley et al. (2019)
<doi:10.1080/10618600.2018.1537924>, Datta et al. (2019)
<doi:10.1214/19-BA1177>, and May and Finley (2025)
<doi:10.1016/j.spasta.2025.100917>.

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
