%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Renvlp
%global packver   3.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Envelope Estimators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-orthogonalsplinebasis 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 
Requires:         R-CRAN-orthogonalsplinebasis 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Matrix 

%description
Provides a general routine, envMU, which allows estimation of the M
envelope of span(U) given root n consistent estimators of M and U. The
routine envMU does not presume a model.  This package implements response
envelopes, partial response envelopes, envelopes in the predictor space,
heteroscedastic envelopes, simultaneous envelopes, scaled response
envelopes, scaled envelopes in the predictor space, groupwise envelopes,
weighted envelopes, envelopes in logistic regression, envelopes in Poisson
regression envelopes in function-on-function linear regression,
envelope-based Partial Partial Least Squares, envelopes with non-constant
error covariance, envelopes with t-distributed errors, reduced rank
envelopes and reduced rank envelopes with non-constant error covariance.
For each of these model-based routines the package provides inference
tools including bootstrap, cross validation, estimation and prediction,
hypothesis testing on coefficients are included except for weighted
envelopes. Tools for selection of dimension include AIC, BIC and
likelihood ratio testing.  Background is available at Cook, R. D.,
Forzani, L. and Su, Z. (2016) <doi:10.1016/j.jmva.2016.05.006>.
Optimization is based on a clockwise coordinate descent algorithm.

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
