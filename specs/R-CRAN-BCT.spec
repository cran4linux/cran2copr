%global packname  BCT
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Context Trees for Discrete Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-igraph 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
An implementation of a collection of tools for exact Bayesian inference
with discrete times series. This package contains functions that can be
used for prediction, model selection, estimation, and other statistical
tasks. Specifically, the functions provided can be used for the exact
computation of the prior predictive likelihood of the data, for the
identification of the a posteriori most likely (MAP) variable-memory
Markov models, for calculating the exact posterior probabilities and the
AIC and BIC scores of these models, and for prediction with respect to
log-loss and 0-1 loss. All the functions here (except generate_data) are
implementations of deterministic algorithms that have linear complexity in
the length of the input data. Example data sets from finance, genetics and
animal communication are also provided. Detailed descriptions of the
underlying theory and algorithms can be found in [Kontoyiannis et al.
'Bayesian Context Trees: Modelling and exact inference for discrete time
series.' <arXiv:2007.14900> [stat.ME], July 2020].

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
