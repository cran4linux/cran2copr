%global packname  stochvol
%global packver   3.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Bayesian Inference for Stochastic Volatility (SV) Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.900
BuildRequires:    R-CRAN-coda >= 0.19
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-coda >= 0.19
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Efficient algorithms for fully Bayesian estimation of stochastic
volatility (SV) models with and without asymmetry (leverage) via Markov
chain Monte Carlo (MCMC) methods. Methodological details are given in
Kastner and Frühwirth-Schnatter (2014) <doi:10.1016/j.csda.2013.01.002>
and Hosszejni and Kastner (2019) <doi:10.1007/978-3-030-30611-3_8>; the
most common use cases are described in Kastner (2016)
<doi:10.18637/jss.v069.i05> and the package vignette.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
