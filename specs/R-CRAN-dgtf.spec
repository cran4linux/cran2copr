%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dgtf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variational and Monte Carlo Inference for Bayesian State-Space Models of Count Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-pg 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Bayesian inference for a general class of state-space models for count
data, providing a unified interface to variational Bayes and Markov chain
Monte Carlo. Models are assembled from modular components for the
observation distribution, link function, gain function, lag distribution,
system equation, and system error, and support Poisson and negative
binomial observations together with seasonality terms. The model class and
the hybrid variational approximation are described in Tang and Prado
(2026) <doi:10.1016/j.csda.2026.108368>.

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
