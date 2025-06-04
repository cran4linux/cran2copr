%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shrinkTVPVAR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Bayesian Inference for TVP-VAR-SV Models with Shrinkage

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-shrinkTVP >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stochvol 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-shrinkTVP >= 3.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stochvol 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-mvtnorm 

%description
Efficient Markov chain Monte Carlo (MCMC) algorithms for fully Bayesian
estimation of time-varying parameter vector autoregressive models with
stochastic volatility (TVP-VAR-SV) under shrinkage priors and dynamic
shrinkage processes. Details on the TVP-VAR-SV model and the shrinkage
priors can be found in Cadonna et al. (2020)
<doi:10.3390/econometrics8020020>, details on the software can be found in
Knaus et al. (2021) <doi:10.18637/jss.v100.i13>, while details on the
dynamic shrinkage process can be found in Knaus and Frühwirth-Schnatter
(2023) <doi:10.48550/arXiv.2312.10487>.

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
