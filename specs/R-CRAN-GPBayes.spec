%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPBayes
%global packver   0.1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Gaussian Process Modeling in Uncertainty Quantification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-stats 
Requires:         R-methods 

%description
Gaussian processes (GPs) have been widely used to model spatial data,
spatio-temporal data, and computer experiments in diverse areas of
statistics including spatial statistics, spatio-temporal statistics,
uncertainty quantification, and machine learning. This package creates
basic tools for fitting and prediction based on GPs with spatial data,
spatio-temporal data, and computer experiments. Key characteristics for
this GP tool include: (1) the comprehensive implementation of various
covariance functions including the Matérn family and the Confluent
Hypergeometric family with isotropic form, tensor form, and automatic
relevance determination form, where the isotropic form is widely used in
spatial statistics, the tensor form is widely used in design and analysis
of computer experiments and uncertainty quantification, and the automatic
relevance determination form is widely used in machine learning; (2)
implementations via Markov chain Monte Carlo (MCMC) algorithms and
optimization algorithms for GP models with all the implemented covariance
functions. The methods for fitting and prediction are mainly implemented
in a Bayesian framework; (3) model evaluation via Fisher information and
predictive metrics such as predictive scores; (4) built-in functionality
for simulating GPs with all the implemented covariance functions; (5)
unified implementation to allow easy specification of various GPs.

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
